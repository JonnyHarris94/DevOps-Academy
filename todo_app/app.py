from flask import Flask,render_template, request, redirect
import todo_app.data.trello_items as trello_items 
import requests

# create flask app
def create_app():
    app = Flask(__name__)
    app.config.from_object('todo_app.flask_config.Config')


    # index route 
    @app.route('/', methods = ["GET"])
    def index():
        cards = trello_items.get_card()
        item_view_model = trello_items.ViewModel(cards)
        return render_template('index.html',view_model=item_view_model)


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

    return app