import PyPDF2

pdf_file = open('hello.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

text_content = ''

for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text_content += page.extract_text()

pdf_file.close()

with open('output1.txt', 'w', encoding='utf-8') as text_file:
    text_file.write(text_content)