from flask import Flask, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    index = open("core\index.html").read()
    return index




def startFlask():
    app.run()
