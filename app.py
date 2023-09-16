from flask import Flask, render_template, request
from bardapi import BardCookies
import datetime
EXPLAIN_TEMPLATE_LOADING = True
app = Flask(__name__)
Cookies_dict={
    "__Secure-1PSIDTS":"sidts-CjEBSAxbGakPKKcI2BxTP6-cKRaShb7fo3HoFXAjdipsR3SoXQT0aSMnOOaEFO6mBdGzEAA",
    "__Secure-1PSID" :"aQjWW1l3CsGHJp9tCROZwwlPadlcFbTB9M81a67mlyRHgECMnZbflncraaEB6LInyHhxLw.",
    "__Secure-1PSIDCC" : "APoG2W_pH-vzg_nR6r9bkv8Zn5u1YAUxaeEn84JfGuDIVfKJLvQc24gOfaazydiF-RR0l42O14Cs" }
@app.route("/", methods=["GET", "POST"])
def index():
    Reply = None
    if request.method == "POST":
        query = request.form["query"]
        names = request.form["names"]
        age = request.form["age"]
        with open("data.txt", "a", encoding="utf-8") as f:
            f.writelines(str(query)+"\n"+str(names)+"\n"+str(age)+"\n"+str(datetime.datetime.now())+"\n")
        with open("data.txt", "r", encoding="utf-8") as f:
            R=f.read()
        R_variable=R

        Bard = BardCookies(cookie_dict=Cookies_dict)
        Reply = Bard.get_answer(R_variable)['content']

        
        return render_template("bard.html", reply=Reply)
    else:
        return render_template("bard.html", reply=Reply)
        

if __name__ == "__main__":
    app.run(debug=True)


