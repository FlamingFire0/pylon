from flask import Flask, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    websitetext = open("core\website.html").read()
    return websitetext





def startFlask():
    app.run()