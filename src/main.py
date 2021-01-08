from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'
todos = ['todo 1', 'todo 2 ', 'todo 3']

@app.route('/')
def index():
    user_ip = request.remote_addr
    responce = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return responce

@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    context = {
        'user_ip':user_ip,
        'todos':todos
    }
    return render_template('hello.html', **context) 

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=8080)