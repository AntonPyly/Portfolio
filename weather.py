import requests


def check_input_city(name: str) -> str:
    return ''.join(i for i in name if i.isalpha() or i in [' ', '-']).capitalize()


def get_weather(name: str, api: str):
    try:
        url_api = f'https://api.openweathermap.org/data/2.5/weather?q={name_clear}&appid={api_name}&units=metric'
        response = requests.get(url_api)
        data_json = response.json()
        return data_json['main']['temp']
    except:
        print('Wrong name api, or wrong name city')


api_name = '33d99a1c99c5ea82e6aaff8592cd6fc3'
des_input = input('Enter something to continue else enter stop: ')
while des_input != 'stop':

    name_of_city = input('Input City:')
    name_clear = check_input_city(name_of_city)
    print(f'Weather in city {name_clear} is {get_weather(name_clear, api= api_name)}')
    des_input = input('Enter something to continue else enter stop: ')
