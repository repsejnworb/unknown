from flask import render_template, redirect
from flask import flash as _flash
from unknown import app
from forms import LoginForm

def flash(message, category='info'):
    _flash(message, category)

def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/')
@app.route('/index')
def index():
    flash("hello")
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for User="' + form.username.data + '", remember_me=' + str(form.remember_me.data), 'info')
        return redirect('/index')
    else:
        flash_errors(form)
    return render_template('login.html', 
        title = 'Sign In',
        form = form)