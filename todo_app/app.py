from flask import Flask,render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item, save_item, get_item
import todo_app.data.trello_items as trello_items 
import requests

# create flask app
app = Flask(__name__)
app.config.from_object(Config)


# index route 
@app.route('/', methods = ["GET"])
def index():
    cards = trello_items.get_card().json()
    return render_template('index.html',cards=cards )

@app.route('/', methods = ["POST"])
def newitem():
    title = request.form.get('title')
    trello_items.add_item(title)
    return redirect('/')

@app.route('/close', methods = ["POST"])
def complete_item():
    id = request.args['id']
    response = trello_items.complete_item(id) 
    return redirect('/')















if __name__ == '__main__':
    app.run(debug = True)
