#clou# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template, redirect
from flask import request
from model import foodAte
from datetime import datetime

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time=datetime.now())


@app.route('/greeting', methods=["POST", "GET"])
def greeting():
    if request.method == "POST":
        user_name = request.form['nickname']
        thebreakfast = request.form['breakfast']
        print(user_name)
        your_nickname=user_name
        your_breakfast= thebreakfast
        rateBreakfast = foodAte(your_breakfast)
        print(your_nickname)
        return render_template("greeting.html", your_nickname = your_nickname, your_breakfast=your_breakfast,rateBreakfast=rateBreakfast)
    else:
        return redirect('/')

@app.route('/owelahs')
def hello():
    return "Welcome to Owelahs"
