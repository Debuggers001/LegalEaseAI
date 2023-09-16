from flask import Flask, render_template, request
from bardapi import BardCookies

app = Flask(_name_)
Cookies_dict={
    "__Secure-1PSIDTS":"sidts-CjEBSAxbGakPKKcI2BxTP6-cKRaShb7fo3HoFXAjdipsR3SoXQT0aSMnOOaEFO6mBdGzEAA",
    "__Secure-1PSID" :"aQjWW1l3CsGHJp9tCROZwwlPadlcFbTB9M81a67mlyRHgECMnZbflncraaEB6LInyHhxLw.",
    "__Secure-1PSIDCC" : "APoG2W_pH-vzg_nR6r9bkv8Zn5u1YAUxaeEn84JfGuDIVfKJLvQc24gOfaazydiF-RR0l42O14Cs" }
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]
        Bard = BardCookies(cookie_dict=Cookies_dict)
        Reply = Bard.get_answer(query)['content']
        with open("data.txt", "w", encoding="utf-8") as f:
            f.writelines(Reply)
        return render_template("index.html", reply=Reply)
    else:
        return render_template("index.html")

if _name_ == "_main_":
    app.run(debug=True)