import urllib.parse
import requests
from .levenstein import check_substring


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
        result.append(data)
    return result


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
    key_skills = key_skills_to_string(vacancy['key_skills'])
    return Vacancy(vacancy_name, employer_name, address, requirements, vacancy_link, key_skills)


def key_skills_to_string(key_skills):
    result = ''
    for skill in key_skills:
        result += skill['name'] + ' '
    return result

#def get_skill_list(json_data):

