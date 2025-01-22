from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def home():
    return 'This is a good app'

@app.route('/method',methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return 'You have used a POST request'
    else:
        return 'You are using a GET request'

app.run()
