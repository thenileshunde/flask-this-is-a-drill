
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello Azure!</h1>"

if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app
