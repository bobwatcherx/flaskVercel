from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
	return "HELLO from vercel use flask"


@app.route("/about")
def about():
	return "HELLO about"
