import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 

# Open the scanned PDF file
pdf_document = fitz.open('Unit 3.pdf')

# Initialize extracted text
extracted_text = ""

# Loop through each page in the PDF
for page_num in range(len(pdf_document)):
    # Extract the PDF page
    page = pdf_document[page_num]

    # Convert the PDF page to an image using PyMuPDF
    pix = page.get_pixmap()

    # Save the image as a temporary file (adjust format as needed)
    image_file = f"temp_page_{page_num}.png"
    pix.save(image_file, "png")

    # Perform OCR on the image using Tesseract
    text = pytesseract.image_to_string(Image.open(image_file), lang='hin')  # 'hin' is the language code for Hindi
    extracted_text += text

    # Clean up temporary image file
    os.remove(image_file)

# Close the PDF document
pdf_document.close()

# Now 'extracted_text' contains the text extracted from the scanned PDF in Hindi
print(extracted_text)
