$pdf_mode = 1;
$out_dir = 'output/pdf';
$interaction = 'nonstopmode';
$file_line_error = 1;

# Only one PDF is ever stored: output/pdf/thesis.pdf, the build output. The repository root
# holds a symlink, thesis.pdf -> output/pdf/thesis.pdf, so the author keeps a stable path to
# open. That symlink is tracked in git, so a fresh clone resolves it without a build. The
# command below only recreates the link if it was deleted or repointed; otherwise it is a no-op
# and the two paths cannot drift apart.
$success_cmd = 'ln -sfn output/pdf/thesis.pdf %R.pdf';
