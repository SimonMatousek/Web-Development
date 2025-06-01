from flask import flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return f"{request.headers=}"

@app.route('/first')
def firs():
    return "First"

@app.route('/second')
def second():
    return "Second"

@app.route('/items/<item_id>')
def items_items_id(item_id):
    return f"Item: {item_id}"


if __name__ == "__main":
    app.run(debug=True)