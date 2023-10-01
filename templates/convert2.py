import fitz  # PyMuPDF
import pytesseract
import os
from PIL import Image
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from bardapi import BardCookies
import re
import mysql.connector
# Open the PDF file
pdf_document = fitz.open('UNIT 2.pdf')

# Initialize Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with the path to your Tesseract executable

# Loop through each page in the PDF
extracted_text = ""
for page_num in range(len(pdf_document)):
    # Extract the PDF page
    page = pdf_document[page_num]  # Use indexing to access the page

    # Convert the PDF page to an image using PyMuPDF
    pix = page.get_pixmap()

    # Save the image as a temporary file (adjust format as needed)
    image_file = f"temp_page_{page_num}.png"
    pix.save(image_file, "png")

    # Perform OCR on the image
    text = pytesseract.image_to_string(image_file)
    # text = pytesseract.image_to_string(Image.open(image_file), lang='hin')
    extracted_text += text

    # Clean up temporary image file
    os.remove(image_file)

# Close the PDF document
pdf_document.close()

# Now 'extracted_text' contains the text extracted from the scanned PDF
with open('output.txt', 'w', encoding='utf-8') as text_file:
    text_file.write(extracted_text)