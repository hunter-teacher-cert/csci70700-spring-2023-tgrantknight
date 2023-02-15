from flask import Flask
from flask import render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("home.html")

@app.route('/lucky')
def lucky():
  numbers = []
  for x in range(0,5):
    numbers.append(random.randrange(100))
  return render_template("lucky.html", nums = numbers)

app.run(host='0.0.0.0', port=81)
