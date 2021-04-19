from flask import Flask,render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item, save_item, get_item


# create flask app
app = Flask(__name__)
app.config.from_object(Config)


# index route 
@app.route('/', methods = ["GET"])
def index():
    items = get_items()
    return render_template('index.html', items = items)

@app.route('/', methods = ["POST"])
def newitem():
    title = request.form.get('title')
    add_item(title)
    return redirect('/')














if __name__ == '__main__':
    app.run(debug = True)
