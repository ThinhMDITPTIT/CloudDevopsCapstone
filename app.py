from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    html = f"<h3>Hello World, my name is ThinhMD (TonyTMD). Welcome to my Cloud Devops Capstone project!</h3>"
    return html.format(format)

if __name__ == "__main__":
    # specify port = 80
    app.run(host='0.0.0.0', port=80, debug=True) 