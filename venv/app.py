from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'This is a good app'

app.run()
