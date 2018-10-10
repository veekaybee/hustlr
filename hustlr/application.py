from flask import Flask, request, render_template
from threading import Timer

import generate_name as gs

application = Flask(__name__)

# Connect to Mongo
mongo = gs.MongoConnection("hn", "syllables")
collection = mongo.get_collection()


# Render main page
@application.route('/')
def index():
    return render_template('index.html')


# Render results of Mongo load
@application.route('/result',methods = ['POST','GET'])
def result():

    items = gs.get_random_doc(collection)

    if request.method == 'GET':
        return render_template("result.html",result=items)


if __name__ == "__main__":
    try:
        gs.load_data(collection)
    except KeyError:
        print("No Port")
    #Timer(3600, gs.load_data(collection)).start()
    application.run()

