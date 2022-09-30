from flask import Flask, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"





def startFlask():
    app.run()
    

if __name__ == "__main__":
    startFlask()