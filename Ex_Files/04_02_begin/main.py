from distutils.log import debug
from flask import Flask # in Terminal run command 'pip install Flask' to install Flask for web application

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, World!"

app.run(debug=True)