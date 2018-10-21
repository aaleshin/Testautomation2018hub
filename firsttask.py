import requests

class Metod:
    def __init__(self):
        name = input("Как тебя зовут?")
        print(name.upper(), ", добро пожаловать в мир Python, раздолбай!")


print("Привет, тестер!")
a = Metod()

r = requests.get('https://planner.thumbtack.net/employees/')
print(r.status_code)
print(r.headers['content-type'])