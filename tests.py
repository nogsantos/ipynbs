from pdfminer.high_level import extract_text

info = extract_text('./data/eng.pdf')

print(info)
