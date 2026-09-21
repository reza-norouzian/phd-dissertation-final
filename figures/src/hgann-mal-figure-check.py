"""Check the numbers printed in the Chapter 5 data figures.

Extracts the text of the included F1 figure and the author-supplied accuracy and distribution
figures with pdftotext. The F1 and accuracy figures are compared with the result tables of content/hgann-mal.tex
(tab:hgann:binary, tab:hgann:multi), and the class-distribution figure with the two dataset
tables of the source publication, which the chapter reprinted until T-006 cut them. Problems
inside a figure are printed as notes and do not fail the check. Run from the repository root:

    python3 figures/src/hgann-mal-figure-check.py
"""
import re
import subprocess
import sys
from pathlib import Path

ASSET = Path('figures/hgann-mal')
SUPPLIED = ASSET / 'supplied'
TEX = Path('content/hgann-mal.tex').read_text()
PUB = next(Path('publications').glob('HGANN*/*.tex')).read_text()
passed, failed, notes, info = [], [], [], []


def text(name, root=SUPPLIED):
    return subprocess.run(['pdftotext', '-layout', str(root / name), '-'],
                          capture_output=True, text=True, check=True).stdout


def check(cond, msg):
    (passed if cond else failed).append(msg)


def note(cond, msg):
    if cond:
        notes.append(msg)


def block(label):
    return TEX.split(r'\label{%s}' % label)[1].split(r'\end{tabular}')[0]


def pub_tabular(label):
    return PUB.split(r'\label{%s}' % label)[0].rsplit(r'\begin{tabular}', 1)[1]


def floats(s):
    return [float(x) for x in re.findall(r'\d+\.\d', s)]


def results(label):
    body = block(label)
    pats = {'GCN': r'^\s*GCN\s*&(.*?)\\\\', 'GraphSAGE': r'^\s*GraphSAGE\s*&(.*?)\\\\',
            'HGNN': r'^\s*HGNN\s*&(.*?)\\\\', 'HGNN+': r'^\s*HGNN\+\s*&(.*?)\\\\',
            'HGANN-Mal': r'^\s*\\hgann\{\}\s*&(.*?)\\\\'}
    rows = {k: floats(re.search(p, body, re.M | re.S).group(1)) for k, p in pats.items()}
    assert all(len(v) == 8 for v in rows.values()), rows
    majority = floats(re.search(r'Majority class(.*?)\\\\', body).group(1))
    return rows, majority


(binary, maj_b), (multi, maj_m) = results('tab:hgann:binary'), results('tab:hgann:multi')
METHODS = ['GCN', 'GraphSAGE', 'HGNN', 'HGNN+', 'HGANN-Mal']
TASKS = [('Drebin binary', binary, 0), ('CICMalDroid binary', binary, 4),
         ('Drebin family', multi, 0), ('CICMalDroid category', multi, 4)]
F1 = {name: [t[m][o] for m in METHODS] for name, t, o in TASKS}
ACC = {name: [t[m][o + 3] for m in METHODS] for name, t, o in TASKS}
MAJ = dict(zip([t[0] for t in TASKS], maj_b + maj_m))

# Metric consistency and the three author-supplied Drebin binary summaries (T-032).
for task, table, offset in TASKS:
    for method in METHODS:
        f1, precision, recall = table[method][offset:offset + 3]
        check(f1 <= (precision + recall) / 2 + 0.1000001,
              f'{task}, {method}: F1 respects the P/R bound within one-decimal rounding')

MATRICES = {
    'GCN': (962, 150, 66, 1828),
    'HGNN': (1049, 63, 33, 1861),
    'HGANN-Mal': (1085, 27, 24, 1870),
}
for method, (tp, fn, fp, tn) in MATRICES.items():
    p_pos, r_pos = tp / (tp + fp), tp / (tp + fn)
    p_neg, r_neg = tn / (tn + fn), tn / (tn + fp)
    f_pos = 2 * p_pos * r_pos / (p_pos + r_pos)
    f_neg = 2 * p_neg * r_neg / (p_neg + r_neg)
    derived = [round(50 * (f_pos + f_neg), 1),
               round(50 * (p_pos + p_neg), 1),
               round(50 * (r_pos + r_neg), 1),
               round(100 * (tp + tn) / (tp + fn + fp + tn), 1)]
    check(derived == binary[method][:4],
          f'Drebin binary {method}: matrix gives F1, P, R, accuracy {derived}')
    check((tp + fn, fp + tn) == (1112, 1894),
          f'Drebin binary {method}: matrix contains 1,112 malicious and 1,894 benign cases')

# F1 figure: bar labels and the gain line.
t2 = text('hgann-mal-f1.pdf', ASSET)
bars = [float(x) for x in re.findall(r'(?<![+\d])(\d{2}\.\d)', t2)]
expected = sum((F1[k] for k in ('Drebin binary', 'Drebin family', 'CICMalDroid binary',
                                'CICMalDroid category')), [])
check(sorted(bars) == sorted(expected), f'F1 figure: {len(bars)} bar labels equal the F1 columns')
order = ('Drebin binary', 'Drebin family', 'CICMalDroid binary', 'CICMalDroid category')
gains = [float(x) for x in re.findall(r'\+(\d\.\d)', t2)]
calc = [round(F1[k][4] - max(F1[k][:4]), 1) for k in order]
check(gains == calc, f'F1 figure: gains over the strongest baseline {gains}')
note('Family classification' in t2.split('(b)')[1],
     'F1 figure, panel (b): the CICMalDroid multiclass task is labelled "Family classification"; '
     'it is malware-category classification')

# Accuracy figure: the four reference points of every row and the printed differences.
t3 = text('fig3-acc-dif.pdf')
for k in ACC:
    for v in (MAJ[k], ACC[k][1], ACC[k][3], ACC[k][4]):
        check(f'{v:.1f}' in t3, f'accuracy figure prints {v:.1f} ({k})')
    check(ACC[k][1] == max(ACC[k][:2]), f'GraphSAGE is the best pairwise operator ({k})')
    check(ACC[k][3] == max(ACC[k][2:4]), f'HGNN+ is the best hypergraph baseline ({k})')
deltas = [round(ACC[k][4] - ACC[k][3], 1) for k in ACC]
printed = [float(x.replace('−', '-')) for x in re.findall(r'·\s*([+−-]\d\.\d)', t3)]
check(printed == deltas, f'accuracy figure: HGANN-Mal minus HGNN+ {printed}')
steps = {k: round(ACC[k][3] - ACC[k][1], 1) for k in ACC}
check((min(steps.values()), max(steps.values())) == (3.8, 6.7),
      f'HGNN+ over GraphSAGE: {sorted(steps.values())} (text: 3.8 to 6.7)')
check(all(steps[k] > ACC[k][4] - ACC[k][3] for k in ACC),
      'the pairwise-to-HGNN+ step exceeds the HGNN+-to-HGANN-Mal difference in all four')
for n in ('15,030', '11,598', '4,664'):
    check(n in t3, f'accuracy figure prints corpus size {n}')

# Class-distribution figure against the dataset tables of the source publication.
t1 = text('hgann-mal-class-distribution_new.pdf')
panel_a, panel_b = t1.split('(b)', 1)
fam_src = {a: int(b) for a, b in re.findall(r'([A-Z][A-Za-z]+)\s*&\s*(\d+)\b',
                                           pub_tabular('table:derbin_dataset'))}
fam_fig = {a: int(b) for a, b in re.findall(r'([A-Z][A-Za-z]+)\s+(\d{2,3})\b', panel_a)
           if a in fam_src}
check(len(fam_src) == 20 and fam_fig == fam_src,
      'twenty family counts agree with the source publication')
check(sum(fam_src.values()) == 4664, 'family counts sum to 4,664')
check('896' in t1 and '159 families' in t1 and 5560 - 4664 == 896 and 179 - 20 == 159,
      '159 families and 896 samples outside the twenty (179 families, 5,560 samples)')
check(f'{100 * 4664 / 5560:.1f}' == '83.9' and f'{100 * 896 / 5560:.1f}' == '16.1',
      'retained 83.9 per cent, left out 16.1 per cent')
check(f'{925 / 41:.1f}' == '22.6', 'largest to smallest family 925 : 41 = 22.6')
cats_src = {c: (int(n.replace(',', '')), float(s)) for c, n, s in re.findall(
    r'(SMS malware|Riskware|Banking|Adware|Benign)\s*&\s*([\d,]+)\s*&\s*([\d.]+)',
    pub_tabular('table:CICMalDroid_dataset'))}
flat = ' '.join(t1.split())
for c, (n, s_pub) in cats_src.items():
    share = round(100 * n / 11598, 1)
    check(f'{c} {n:,}' in flat, f'category {c} {n:,} as in the source publication')
    check(f'{share:.1f}' in panel_b, f'figure prints the share of {c} as {share:.1f} per cent')
    if s_pub != share:
        info.append(f'the source publication prints {c} as {s_pub} per cent; {n:,} of 11,598 '
                    f'rounds to {share:.1f}, which the figure and the chapter use')
check(len(cats_src) == 5 and sum(n for n, _ in cats_src.values()) == 11598,
      'five categories sum to 11,598')
check(f'{100 * 11598 / 17341:.1f}' == '66.9', '11,598 of 17,341 = 66.9 per cent')
check(round(3904 / 1253, 1) == 3.1, 'largest to smallest category 3.1 : 1 (text)')
check(round(100 * max(fam_src.values()) / 4664, 1) == MAJ['Drebin family'],
      'majority baseline of the family task = 925 / 4,664')
check(round(100 * max(n for n, _ in cats_src.values()) / 11598, 1) == MAJ['CICMalDroid category'],
      'majority baseline of the category task = 3,904 / 11,598')

print(f'{len(passed)} passed, {len(failed)} failed, {len(notes)} notes')
for m in failed:
    print('FAIL', m)
for m in notes:
    print('note', m)
for m in info:
    print('info', m)
sys.exit(1 if failed else 0)
