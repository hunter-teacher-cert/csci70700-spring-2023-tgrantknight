from flask import Flask
from flask import render_template
from flask import session
import random

app = Flask(__name__)
app.secret_key = "somethingXD"


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

