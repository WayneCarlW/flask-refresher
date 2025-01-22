from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weight=''
    height=''

    if request.method == 'POST' and 'weightbox' and 'heightbox' in request.form:
        weight = int(request.form.get('weightbox'))
        height = int(request.form.get('heightbox'))
    
    return render_template('index.html',
            weight=weight,
            height=height)

app.run(debug=True)
