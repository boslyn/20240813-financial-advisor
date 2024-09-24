from flask import Flask,render_template,request
import google.generativeai as genai
import os

api = os.getenv("MAKERSUITE_API_TOKEN")
model=genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/financial_QA", methods=["GET","POST"])
def financial_QA():
    return(render_template("financial_QA.html"))

@app.route("/makersuite", methods=["GET","POST"])
def makersuite():
    q=request.form.get("q")
    r = model.generate_content(q)
    return(render_template("makersuite.html",r=r.text))

""" @app.route("/prediction", methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html")) """

@app.route("/singapore_joke", methods=["GET","POST"])
def singapore_joke():
    return(render_template("singapore_joke.html"))


if __name__ == "__main__":
    app.run()

