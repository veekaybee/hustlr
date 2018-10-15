from flask import Flask, request, render_template, url_for
from threading import Timer, Thread
import generate_name as gs


application = Flask(__name__)



# Render main page
@application.route('/index/')
@application.route('/')
def index():
    return render_template('index.html')


@application.route('/about/')
def about():
    return render_template('about.html')


# Render results of Mongo load
@application.route('/result',methods = ['POST','GET'])
def result():
    mongo = gs.MongoConnection("hn", "syllables")
    collection = mongo.get_collection()
    items = gs.get_random_doc(collection)

    if request.method == 'GET':
        return render_template("result.html",result=items)


if __name__ == "__main__":
    application.run()

