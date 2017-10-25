
from flask import Flask, request, render_template, make_response,redirect, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required, Email

import requests
import json

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'hard to guess string'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')
    
@app.route('/')
def first():
    return redirect(url_for('cookie_insertion'))

# This route is a good example
@app.route('/user/<name>')
def hello_user(name):
   return '<h1>Hello {0}</h1>'.format(name)

@app.route('/set_cookie')
def cookie_insertion():
    chocolatechipcookie = redirect('/form')
    response = make_response(chocolatechipcookie)  
    response.set_cookie('chocolatechipcookie',value="TRUE")
    return response


@app.route('/surpise',methods= ['POST','GET'])
def surprise():
    return render_template("newtemplate.html")


@app.route('/form',methods= ['POST','GET'])
def enter_data():
    return render_template("template2.html")


@app.route('/newresult',methods = ['POST', 'GET'])
def res2():
    if request.method == 'GET':
        cookies = request.cookies.get('chocolatechipcookie')
        newresult = request.args
        nfirst = newresult.get('firstname')
        first= str(nfirst) + "is "
        newnumm = newresult.get('number')
        data = { 
            "title" : "This is our result page",
            "name": nfirst, 
            "age":newnumm,
            "cookie":cookies

        }
        response = make_response(render_template("blank_template.html",result = data))  
        response.set_cookie('name',value=nfirst)
        return response
        #return "<b>" + first + "</b> <i>" + str("was born in ") + newage + str("!") + "</i>" 


class PuppyForm(FlaskForm):
    puppy = StringField('Enter your favorite type of puppy to get fun pictures of other dogs.', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/puppy')
def index():
    simpleForm = PuppyForm()
    return render_template('wtf.html', form=simpleForm)

@app.route('/puppyresult', methods = ['GET', 'POST'])
def result():
    form = PuppyForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        puppy = form.puppy.data
        favoritepuppy =  "Your favorite puppy is a {0}! ".format(puppy)
        return render_template("puppypictures.html", result= favoritepuppy)
    flash('All fields are required!')
    return redirect(url_for('index'))
#done

if __name__ == '__main__':
    app.run()