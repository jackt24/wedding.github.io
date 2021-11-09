from flask import Flask, render_template, url_for
import smtplib

from flask.wrappers import Request
from werkzeug.wrappers import request

app = Flask(__name__)
# app = Flask(static_folder="C:\Users\Lana\Desktop\Anoxide\anoxide.github.io\anoxide_app\static")



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def form():
    name = request.form.get("name")
    email = request.form.get("email")
    special = request.form.get("special")

    message = "Thank you for your response, please call Jack on 07850046333 if there are any issues"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("jackt2469@gmail.com", "Youerb69@")
    server.sendmail("jackt2469@gmail.com", email, message)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)