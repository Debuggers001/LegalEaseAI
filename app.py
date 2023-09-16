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
        address=request.form["address"]
        with open("data.txt", "w", encoding="utf-8") as f:
            f.writelines("i want to file a case so create a draft application for me in totally legal format and also mention the IPC section and every analysis of the case, also mention the details i am giving to you, and don't mention anything about police station, here are the details:")
            f.writelines("what happened with me:"+str(query)+"\n"+"my name:"+str(names)+"\n"+"my age:"+str(age)+"\n"+"date and time on which it happened :"+str(datetime.datetime.now())+"\n"+"your address:"+str(address))
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