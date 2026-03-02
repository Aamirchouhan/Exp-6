from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Aamir_Chouhan<h1<br><h2>AppID = 2410491</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)