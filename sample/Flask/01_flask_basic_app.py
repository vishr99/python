# from django.views import debug
# from flask import  Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello():
#     return 'Hello World'
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return '<h2>Welcome %s</h2>' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)