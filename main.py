import json

from flask import Flask

import function

app = Flask(__name__)


@app.route('/')
def main():
    candidates_list = function.get_candidates("data/candidates.json")

    return function.questionnaire_candidates(candidates_list)


@app.route('/candidates/<candidate_id>')
def page_candidate(candidate_id):
    candidates_list = function.get_candidates("data/candidates.json")
    candidate = function.get_id_candidate(candidates_list, candidate_id)
    photo = f'<img src="{candidate["picture"]}">'
    return photo + function.questionnaire_candidates([candidate])


@app.route('/skills/<skill>')
def skills(skill):
    candidates_list = function.get_candidates("data/candidates.json")

    return function.questionnaire_candidates(function.get_skill_candidates(candidates_list, skill))


app.run()
