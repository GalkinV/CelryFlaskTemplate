from flask import Flask
from app.main import main

app = Flask(__name__)
app.register_blueprint(main)
print(app)
