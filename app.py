import os

from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

import generate_name as gs


app = Flask(__name__)

# Connect to Mongo
mongo = gs.MongoConnection("hn", "syllables")
collection = mongo.get_collection()


# Render main page
@app.route('/')
def index():
    return render_template('index.html')


# Render results of Mongo load
@app.route('/result',methods = ['POST','GET'])
def result():

    items = gs.get_random_doc(collection)

    if request.method == 'GET':
        return render_template("result.html",result=items)


if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0')