from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash

import unittest  

from app import create_app
from app.forms import TodoForm, DeleteTodoForm

from app.firestore_service import get_users, get_todos, put_todo, delete_todo
from flask_login import login_required, current_user

app = create_app()


@app.route('/')
def index():
    user_ip = request.remote_addr
    responce = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return responce


@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteTodoForm()

    context = {
        'user_ip':user_ip,
        'todos':get_todos(user_id=username),
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form,
    }

    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data)
        flash('La tarea se creo con exito')

        return redirect(url_for('hello'))

    return render_template('hello.html', **context) 


@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id,todo_id=todo_id)

    return redirect(url_for('hello'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

if __name__ == "__main__":
    app.run()