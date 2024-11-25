from flask import Flask
from controllers.controller import app_blueprint
import os

app = Flask(__name__, template_folder='views')
app.secret_key = os.urandom(24)
app.register_blueprint(app_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
