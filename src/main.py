from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['todo 1', 'todo 2 ', 'todo 3']

@app.route('/')
def index():
    user_ip = request.remote_addr
    responce = make_response(redirect('/hello'))
    responce.set_cookie('user_ip', user_ip)

    return responce

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip':user_ip,
        'todos':todos
    }
    return render_template('hello.html', **context)

@app.route('/sucho')
def sucho():
    return "hola desde Sucho"