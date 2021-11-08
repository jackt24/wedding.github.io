from flask import Flask, render_template, url_for

app = Flask(__name__)
# app = Flask(static_folder="C:\Users\Lana\Desktop\Anoxide\anoxide.github.io\anoxide_app\static")



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)