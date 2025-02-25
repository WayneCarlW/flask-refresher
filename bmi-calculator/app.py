from flask import Flask, request, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bnE6I8CVMTyF3T7fa1RUook8VoDX88z0'

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

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
