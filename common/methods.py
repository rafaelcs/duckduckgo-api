import requests


class Methods:
    def __init__(self):
        self.request_url = 'https://api.duckduckgo.com/?q=simpsons%20characters&format=json&pretty=1'

    def get(self):
        api_response = requests.get(url=self.request_url)
        return api_response
