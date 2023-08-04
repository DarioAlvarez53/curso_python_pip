import requests # requests es una libreria que nos ayuda a trabajar con http api para poder consumir e iterar datos

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category['name'])