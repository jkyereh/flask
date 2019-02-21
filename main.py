import flask
from flask import Flask, render_template

app = Flask(__name__)
from app import routes

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/index')
def index():
    return "Hello, World!"
    
app.route('contact')
def contact():
    return"Contact us Babe"
    
if __name__ == "__main__":
    app.run(debug=True)
    