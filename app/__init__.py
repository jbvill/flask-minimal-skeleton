from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__, )

app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
lm.session_protection = "basic"
login_serializer = URLSafeTimedSerializer(app.secret_key)
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(403)
def forbidden(error):
    return render_template("403.html"), 403

@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500
    
from app.auth.views import auth
from app.admin.views import admin
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(admin, url_prefix='/admin')

db.create_all()