import requests


def test_celery():
    requests.get('http://127.0.0.1:8000/hello-world?name=Vitalii')
    requests.get('http://127.0.0.1:8000/hello-world?name=Ivan')
    requests.get('http://127.0.0.1:8000/hello-world?name=Vlad')


if __name__ == '__main__':
    test_celery()