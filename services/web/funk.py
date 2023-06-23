import requests
import json


def appeal(figure):
    d = {"count": figure}
    question = requests.get("https://jservice.io/api/random?", params=d)
    answers = json.loads(question.text)
    dictt = {}
    for answer in answers:
        dictt.update(answer)
        return dictt
