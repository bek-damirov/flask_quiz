from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(), unique=True)
    answer = db.Column(db.String())
    created_date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


@app.route("/")
def hello_world():
    return jsonify(hello="world")
