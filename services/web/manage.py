from flask.cli import FlaskGroup
from flask import render_template, request
from project import app, db, Question
from funk import appeal
import requests
import json


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(Question(question="A hearty gut chuckle", answer="Bellylaugh"))
    db.session.commit()


@app.route('/forms')
def form():
    return render_template('forms.html')


@app.route('/answers', methods=['POST', 'GET'])
def get_questions():
    if request.method == 'GET':
        q = Question.query.all()

    if request.method == 'POST':
        number = request.form['number']
        data = {"count": number}
        question = requests.get("https://jservice.io/api/random?", params=data)
        answers = json.loads(question.text)
        db_data = db.session.query(Question.question).all()
        for db_d in db_data:
            for i in range(len(answers)):
                if answers[i]["question"] == db_d[0]:
                    del answers[i]
                    result2 = appeal(1)
                    answers.append(result2)
                    break

        for ans in answers:
            new_data = Question(question=ans["question"], answer=ans["answer"])
            db.session.add(new_data)
            db.session.commit()
        entities = Question.query.order_by(Question.created_date.desc()).limit(number).all()
        return render_template('answers.html', entities=entities)
    return render_template('answers.html', entities=q)


if __name__ == "__main__":
    cli()
