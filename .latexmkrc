$pdf_mode = 1;
$out_dir = 'output/pdf';
$interaction = 'nonstopmode';
$file_line_error = 1;

# Every successful compile leaves two copies of the PDF: the canonical build output in
# output/pdf/thesis.pdf and a copy at the repository root, which is the file the author opens.
# Both are tracked, so a rebuild shows up in git either way.
$success_cmd = 'cp %D %R.pdf';
