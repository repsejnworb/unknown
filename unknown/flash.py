from flask import flash as _flash

SUCCESS = 'success'
INFO = 'info'
WARNING = 'warning'
ERROR = DANGER = 'danger'

def flash(message, category='info'):
    _flash(message, category)

def success(message):
    flash(message, SUCCESS)

def info(message):
    flash(message, INFO)

def warning(message):
    flash(message, WARNING)

def error(message):
    flash(message, ERROR)

def danger(message):
    flash(message, DANGER)

def errors(form):
    """Flashes form errors"""
    for field, _errors in form.errors.items():
        for _error in _errors:
            error(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                _error))