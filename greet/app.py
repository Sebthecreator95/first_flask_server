from flask import Flask
app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "Welcome to my first server!"

@app.route("/welcome/home")
def welcome_home():
    return "Welcome HOME!"

@app.route("/welcome/back")
def welcome_back():
    return "Welcome back?"

