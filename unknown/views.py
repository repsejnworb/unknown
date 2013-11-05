from flask import render_template, redirect
from forms import LoginForm
from unknown import app
from unknown import flash


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash.success('Users: "%s" | Password: "%s" | Remember: "%s"' % (form.username.data, form.password.data, str(form.remember_me.data)))
        return redirect('/index')
    else:
        flash.errors(form)
    return render_template('login.html', 
        title = 'Sign In',
        form = form)