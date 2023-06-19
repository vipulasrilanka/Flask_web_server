from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Python Flask Web service"


# Route decorator used to define the callable object for WSGI
@app.route("/contact-us")
def contact_us():
    text = "How to contact us..!"
    return text

@app.route("/get")
def get():
    return "get call"


if __name__ == "__main__":
        app.run(host="0.0.0.0", port=80, debug=True)

