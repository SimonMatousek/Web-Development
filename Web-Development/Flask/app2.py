from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/numbers/')
def numbers():
    number: list[int] = [1,2,3,4]
    return render_template('numbers.html', number=number)

@app.route('/names/')
def names():
    names: list[str] = ['simon','michalis','raphael','tina']
    return render_template('names.html', names=names)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
    name: str = request.args.get('name')
    password: str = request.args.get('password')
    return render_template('thank_you.html', name=name, password=password)

if __name__=='__main__':
    app.run(debug=True)