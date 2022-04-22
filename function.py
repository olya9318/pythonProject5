import json


def get_candidates(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def questionnaire_candidates(candidates_list):
    data = '<pre>'
    for candidates in candidates_list:
        data += (
            f'Имя кандидата - {candidates["name"]}\n'
            f'Позиция кандидата - {candidates["position"]}\n'
            f'Навыки через запятую - {candidates["skills"]}\n\n'
        )
    data += '<pre>'

    return data


def get_id_candidate(candidates_list, candidate_id):
    candidate_id = int(candidate_id)
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate


def get_skill_candidates(candidates_list, candidate_skill):
    result = []
    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(', ')
        if candidate_skill in candidate_skills:
            result.append(candidate)

    return result
