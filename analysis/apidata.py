import urllib.parse
import requests
from .levenstein import check_substring


def get_api_data():
    main_api = 'https://api.hh.ru/vacancies?'
    text = 'продуктовый аналитик'
    area = '3'  # Ekaterinburg
    area2 = '1'  # Moscow
    per_page = 100
    result = []

    url1 = main_api + urllib.parse.urlencode({'text': text, 'area': area2, 'per_page': per_page})
    url = main_api + urllib.parse.urlencode({'text': text, 'area': area, 'per_page': per_page})
    json_data = requests.get(url).json().get('items') + requests.get(url1).json().get('items')
    for j in json_data:
        if check_substring(text, j['name'].lower(), 1):
            data = prepare_data(j)
            result.append(data)
            '''models.VacancyData.objects.Create(vacancy_name=data['vacancy_name'], employer_name=data['employer_name'],
                                              address=data['address'], requirements=data['requirements'],
                                              vacancy_link=data['vacancy_link'])'''
    return result


class Vacancy:
    def __init__(self, vacancy_name, employer_name, address, requirements, vacancy_link):
        self.vacancy_name = vacancy_name
        self.employer_name = employer_name
        self.address = address
        self.requirements = requirements
        self.vacancy_link = vacancy_link


def prepare_data(vacancy):
    vacancy_name = vacancy['name']
    employer_name = vacancy['employer']['name']
    address = vacancy['area']['name']
    requirements = str(vacancy['snippet']['requirement'] + vacancy['snippet']['responsibility'])\
        .replace('<highlighttext>', '').replace('</highlighttext>', '')
    vacancy_link = vacancy['alternate_url']
    return Vacancy(vacancy_name, employer_name, address, requirements, vacancy_link)



print(get_api_data())