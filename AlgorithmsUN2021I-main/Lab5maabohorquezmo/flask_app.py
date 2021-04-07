#source: https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-es
#app.py
import random
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    r = random.randint(0,10000)
    return render_template('index.html',r=r)