import requests


def getUsersData():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response


def getBooksData():
    """ calling another python microservice , make sure you start below repo in your local
    please start https://github.com/PrudhviPeyyala/python-django-restapi-docker-demo project"""

    url = "http://localhost:8000/book/api/"
    response = requests.get(url)
    return response.json()


def postBookInfo(request):
    url = "http://localhost:8000/book/api/test"
    data = {
        'name': request.data.get('name'),
        'author': request.data.get('author')
    }
    response = requests.post(url, data=data)
    return response.json()
