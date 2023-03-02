from flask import Flask
from flask import render_template
from flask import session
from flask import request
import random

app = Flask(__name__)
app.secret_key = "somethingXD"

@app.route('/form',methods=["GET","POST"])
def form():
  if request.method == "GET":
    return render_template("form.html")
  else:
    username = request.form['username']
    password = request.form['password']

    if username == "Taylor" and password == "Cool":
      return "<h1>Log in successful</h1>"
    else:
      return "<h1>INCORRECT CREDENTIALS</h1>"
    
    # print(request.form)
    # item = request.form['TODO']
    # if "todo_list" not in session:
    #   session['todo_list'] = []

    # if request.form['submit']=='doit':
    #   l = session['todo_list']
    #   l.append(item)
    #   session['todo_list'] = l
    # else:
    #   session['todo_list'] = []

@app.route('/')
def index():
  if "count" not in session:
    session["count"] = 0
  session["count"] += 1
  return render_template("home.html",session=session)

@app.route('/lucky')
def lucky():
  numbers = []
  for x in range(0,5):
    numbers.append(random.randrange(100))
  return render_template("lucky.html", nums = numbers)

app.run(host='0.0.0.0', port=81)

