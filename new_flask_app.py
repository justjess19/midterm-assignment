
from flask import Flask, request, render_template
app = Flask(__name__)
app.debug = True


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

    
@app.route('/')
def hello_world():
    return '<h1>Hello there!</h1>'

# This route is a good example
@app.route('/user/<name>')
def hello_user(name):
   return '<h1>Hello {0}</h1>'.format(name)

@app.route('/form',methods= ['POST','GET'])
def enter_data():
    return render_template("template2.html")


@app.route('/newresult',methods = ['POST', 'GET'])
def res2():
    if request.method == 'GET':
        newresult = request.args
        nfirst = newresult.get('firstname')
        first= str(nfirst) + "is "
        newnumm = newresult.get('number')
        age = 2017 - (int(newnumm))
        newage= str(age)
        return render_template("blank_template.html",result = newresult)
        return render_template("blank_template.html",result = newresult)
        #return "<b>" + first + "</b> <i>" + str("was born in ") + newage + str("!") + "</i>" 


if __name__ == '__main__':
    app.run()