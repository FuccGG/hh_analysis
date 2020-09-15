import urllib.parse
import requests



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
        print(j)

get_api_data()
