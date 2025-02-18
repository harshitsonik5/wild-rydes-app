from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Wild Rydes - Developer: Harshit Sonik - Student ID: 100942462"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
