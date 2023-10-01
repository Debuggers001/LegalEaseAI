from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from bardapi import BardCookies
import re
import mysql.connector
# import fitz  # PyMuPDF
# import pytesseract
# import os
# from PIL import Image
EXPLAIN_TEMPLATE_LOADING = True
app = Flask(__name__)
else_conditon="Page Not Found"
Cookies_dict={
    "__Secure-1PSIDTS":"sidts-CjEB3e41hbwMBHIOU7GDXLc85XQOywVSts9hPXjJSUdVmQNuIhQ5npqjMfUGQPNP0j9_EAA",
    "__Secure-1PSID" :"bAjWWxsTWfSE_99Pg3rNnCzk7GpU7gAapY8lN3I1V2aQgjX4Iu-n9nugUGFlj7K3s5HZYA.",
    "__Secure-1PSIDCC" : "APoG2W9uD_qn4X09s4XfD6HR8osuvNm0G4FbbzCdXM8PD2CpxefVtShM3gudWnKvo9qDwWgx8GpB" }
@app.route("/", methods=["GET", "POST"])
def index():
    Reply = ""
    if request.method == "POST":
        names = request.form["names"]
        gender = request.form["gender"]
        fname = request.form["fname"]
        age = request.form["age"]
        query = request.form["query"]
        noc = request.form["noc"]
        fnameoc = request.form["fnameoc"]
        rwc = request.form["rwc"]
        doi = request.form["doi"]
        toi = request.form["toi"]
        place = request.form["poi"]
        address = request.form["address"]
        pn = request.form["pn"]
        witnesses = request.form["witnesses"]
        evidence = request.form["evidence"]
        injuries = request.form["injuries"]
        loss = request.form["loss"]
        aoc = request.form["aoc"]
        city = request.form["city"]        
        with open("data.txt", "w", encoding="utf-8") as f:
            f.writelines("I want to file a case so create a draft application for me in totally legal format and also mention the IPC section, also mention the details I am giving to you, and don't mention anything about police station and case number. Also don't include or mention anyone's signature in the application. Here are the details:"+"\n"
            +"my name:"+str(names)+"\n"
            +"my gender:"+str(gender)+"\n"
            +"my father's name:"+str(fname)+"\n"
            +"my age:"+str(age)+"\n"
            +"what happened with me:"+str(query)+"\n"
            +"name of culprit :"+str(noc)+"\n"
            +"father's name of culprit:"+str(fnameoc)+"\n"
            +"relation with culprit:"+str(rwc)+"\n"
            +"address of culprit:" + str(aoc)+"\n"
            +"date of incident:"+str(doi)+"\n"
            +"time of incident:"+str(toi)+"\n"
            +"place of incident:"+str(place)+"\n"
            +"my address:"+str(address)+"\n"
            +"My city/district:" + str(city)+"\n"
            +"my mobile number:"+str(pn)+"\n"
            +"my witnesses:"+str(witnesses)+"\n"
            +"evidence:"+str(evidence)+"\n"
            +"my injuries:"+str(injuries)+"\n"
            +"loss i have to face:"+str(loss)+"\n")
        with open("data.txt", "r", encoding="utf-8") as f:
            R=f.read()
        R_variable=R

        Bard = BardCookies(cookie_dict=Cookies_dict)
        Reply = Bard.get_answer(R_variable)['content']
        with open("data2.txt", "w", encoding="utf-8") as f:
            f.writelines(Reply)

        def remove_bold(text):
            return re.sub(r'\**', '', text)

        def main():
        
            with open('data2.txt', 'r') as f:
                text = f.read()

            text = remove_bold(text)

            with open('data3.txt', 'w') as f:
                f.write(text)
        main()
        with open("data3.txt", "r", encoding="utf-8") as f:

            read=f.read()
        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="legalease"
        )

        cursor = db.cursor()

        # Insert applicant details into the table
        sql = "INSERT INTO applicants (name, gender, age, query, noc, rwc, doi, toi, poi, address, pn, witnesses, evidence, injuries, loss, aoc, city) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (names, gender, age, query, noc, rwc, doi, toi, place, address, pn, witnesses, evidence, injuries, loss, aoc, city)
        cursor.execute(sql, values)

        db.commit()

        # Close the database connection
        db.close()
        
        
        return render_template("draft.html", reply=read)    
    else:
        return render_template("bard.html", reply=Reply)
    
@app.route('/custom', methods=['GET'])
def index1():
    with open("data3.txt", "r", encoding="utf-8") as f:
        read=f.read()
    with open("custom.html", "w", encoding="utf-8") as f:
        f.writelines(read)

    return render_template("custom.html", reply=read)


@app.route('/update', methods=['POST'])
def update():
    update = request.form["updatedDraft"]

    with open("data3.txt", "w", encoding="utf-8") as f:
        f.writelines(update)
    return render_template("thankyou.html")

# @app.route('/simplify', methods=['POST'])
# def simplify():
#     pdf = request.form["pdfFile"]
#     # Open the PDF file 
#     pdf_document = fitz.open(pdf)

#     # Initialize Tesseract
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with the path to your Tesseract executable

#     # Loop through each page in the PDF
#     extracted_text = ""
#     for page_num in range(len(pdf_document)):
#         # Extract the PDF page
#         page = pdf_document[page_num]  # Use indexing to access the page

#         # Convert the PDF page to an image using PyMuPDF
#         pix = page.get_pixmap()

#         # Save the image as a temporary file (adjust format as needed)
#         image_file = f"temp_page_{page_num}.png"
#         pix.save(image_file, "png")

#         # Perform OCR on the image
#         text = pytesseract.image_to_string(image_file)
#         # text = pytesseract.image_to_string(Image.open(image_file), lang='hin')
#         extracted_text += text

#         # Clean up temporary image file
#         os.remove(image_file)

#         # Close the PDF document
#         pdf_document.close()
#         return render_template("legalsimplifierFinal.html", new = extracted_text)
if __name__ == "__main__":
    app.run(debug=True)

