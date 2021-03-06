import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'unknown/db/unknown.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'unknown/db/migrations')

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'