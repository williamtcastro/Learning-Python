from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "ASCII Converter"

@app.route("/will")
def will():
    return "Hello William"

if __name__ == "__main__":
    app.run()