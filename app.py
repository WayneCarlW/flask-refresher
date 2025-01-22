from flask import Flask,request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    name = ''
    if request.method == 'POST' and 'namefield' in request.form:
        name = request.form.get('namefield')
    return render_template('index.html',
                            name=name)

#@app.route('/method',methods=['GET', 'POST'])
#def method():
#    if request.method == 'POST':
#        return 'You have used a POST request'
#    else:
#        return 'You are using a GET request'

app.run()
