import urllib.parse
import requests
from collections import Counter
from .levenstein import check_substring
import copy
import operator
#from .models import Vacancy


def get_api_data():
    main_api = 'https://api.hh.ru/'
    vacancies_url = 'vacancies?'
    vacancy_url = 'vacancies/'
    text = 'продуктовый аналитик'
    area = '3'  # Ekaterinburg
    area2 = '1'  # Moscow
    per_page = 100
    ids = []
    result = []
    json_data_1 = []
    key_skills_list = []
    url1 = main_api + vacancies_url + urllib.parse.urlencode({'text': text, 'area': area2, 'per_page': per_page})
    url = main_api + vacancies_url + urllib.parse.urlencode({'text': text, 'area': area, 'per_page': per_page})
    json_data = requests.get(url).json().get('items') + requests.get(url1).json().get('items')

    for j in json_data:
        if check_substring(text, j['name'].lower(), 1):
            ids.append(j['id'])
    for id in ids:
        url2 = main_api + vacancy_url + str(id)
        json_data_1.append(requests.get(url2).json())
    for j in json_data_1:
        data = prepare_data(j)
        key_skills_list.extend(data[1])
        result.append(data[0])
    skill_frequencies = skill_dict_to_text(sort_skill_dict_by_value(dict(Counter(key_skills_list))))
    return result, skill_frequencies


def sort_skill_dict_by_value(skill_dict):
    return {k: v for k, v in sorted(skill_dict.items(), key=lambda item: item[1], reverse=True)}

class Vacancy:
    def __init__(self, vacancy_name, employer_name, address, requirements, vacancy_link, key_skills):
        self.vacancy_name = vacancy_name
        self.employer_name = employer_name
        self.address = address
        self.requirements = requirements
        self.vacancy_link = vacancy_link
        self.key_skills = key_skills


def prepare_data(vacancy):
    vacancy_name = vacancy['name']
    employer_name = vacancy['employer']['name']
    address = vacancy['area']['name']
    requirements = vacancy['description']
    vacancy_link = vacancy['alternate_url']
    key_skills = copy.copy(key_skills_string_and_list(vacancy['key_skills']))
    return Vacancy(vacancy_name, employer_name, address, requirements, vacancy_link, key_skills[0]), key_skills[1]


def key_skills_string_and_list(key_skills):
    result = ''
    skill_list = []
    for skill in key_skills:
        result += skill['name'] + ' '
        skill_list.append(skill['name'])
    return result, skill_list


def skill_dict_to_text(dictionary):
    result = ''
    for item in dictionary:
        result += '<li>' + item + ' - ' + str(dictionary[item]) + '</li>'
    return result


