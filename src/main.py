from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest  


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'
app.config['WTF_CSRF_ENABLED']=False
todos = ['todo 1', 'todo 2 ', 'todo 3']

class LoginForm (FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


@app.route('/')
def index():
    user_ip = request.remote_addr
    responce = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return responce


@app.route('/hello', methods=['POST', 'GET'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip':user_ip,
        'todos':todos,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash("Nombre de usuario registrado con exito")
        return redirect(url_for('index'))

    return render_template('hello.html', **context) 


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=8080)