from unknown import db
from werkzeug import generate_password_hash, check_password_hash

ROLES = {
    "user": 0,
    "admin": 1
}
ROLES_LOOKUP = {}
for key, value in ROLES.iteritems():
    ROLES_LOOKUP[value] = key

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))
    email = db.Column(db.String(128), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=ROLES['user'])
    servers = db.relationship('Server', backref='owner', lazy='dynamic')

    def __init__(self, username, password, email, role):
        self.username = username.title()
        self.role = role
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<Name: %r (role: %r)>' % (self.username, ROLES_LOOKUP[self.role])


class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    comment = db.Column(db.String(256))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Name %r>' % (self.name)
