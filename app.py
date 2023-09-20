from flask import Flask, render_template, request
from bardapi import BardCookies
import datetime
import re
EXPLAIN_TEMPLATE_LOADING = True
app = Flask(__name__)
else_conditon="Page Not Found"
Cookies_dict={
    "__Secure-1PSIDTS":"sidts-CjEBSAxbGakPKKcI2BxTP6-cKRaShb7fo3HoFXAjdipsR3SoXQT0aSMnOOaEFO6mBdGzEAA",
    "__Secure-1PSID" :"aQjWW1l3CsGHJp9tCROZwwlPadlcFbTB9M81a67mlyRHgECMnZbflncraaEB6LInyHhxLw.",
    "__Secure-1PSIDCC" : "APoG2W_pH-vzg_nR6r9bkv8Zn5u1YAUxaeEn84JfGuDIVfKJLvQc24gOfaazydiF-RR0l42O14Cs" }
@app.route("/", methods=["GET", "POST"])
def index():
    Reply = ""
    if request.method == "POST":
        names = request.form["names"]
        gender = request.form["gender"]
        age = request.form["age"]
        query = request.form["query"]
        noc = request.form["noc"]
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
            f.writelines("I want to file a case so create a draft application for me in totally legal format and also mention the IPC section, also mention the details I am giving to you, and don't mention anything about police station and case number. Also don't include or mention anyone's signature in the application. Here are the details:"+"\n")
            f.writelines("my name:"+str(names)+"\n"+"my gender:"+str(gender)+"\n"+"my age:"+str(age)+"\n"+"what happened with me:"+str(query)+"\n"+"name of culprit :"+"\n"+str(noc)+"\n"+"relation with culprit:"+str(rwc) + "address of culprit:" + str(aoc) + "\n" +"\n"+"date of incident:"+str(doi)+"\n"+"time of incident:"+str(toi)+"\n"+"place of incident:"+str(place)+"\n"+"my address"+str(address)+"\n" + "My city / district:" + str(city) + "\n" +"my mobile number"+str(pn)+"\n"+"my witnesses:"+str(witnesses)+"\n"+"evidence:"+str(evidence)+"\n"+"my injuries:"+str(injuries)+"\n"+"loss i have to face:"+str(loss)+"\n" )
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
        #with open("draft.html", "w", encoding="utf-8") as f:
         #    f.writelines(read)
        
        
        return render_template("draft.html", reply=read)
    
    else:
        return render_template("bard.html", reply=Reply)
        

if __name__ == "__main__":
    app.run(debug=True)