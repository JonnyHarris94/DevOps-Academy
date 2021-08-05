import requests
import os

class Card:

    def __init__(self, id, status, title ):
        self.id = id 
        self.name = title
        self.status = status

class ViewModel:
    def __init__(self, items):
        self._items = items
    @property
    def items(self):
        return self._items
    @property
    def todoitems(self):
        return []

def get_card():
    url = "https://api.trello.com/1/boards/N46znsdT/cards"

    query = {
            'key': os.environ.get('TrelloAPI'),
            'token': os.environ.get('TrelloToken')
    }
    response = requests.get(url,params=query).json()
    cards = []
    for item in response:
        cards.append(Card(item['id'],item['idList'],item['name']))
    return cards

def add_item(name):
    url = "https://api.trello.com/1/cards"

    query = {
                'key': os.environ.get('TrelloAPI'),
                'token': os.environ.get('TrelloToken'),
                'idList': '60c73323b5d71d7a754a20fc',
                'name': name
    }
    return requests.post(url,data=query)

def complete_item(id):
    url = f"https://api.trello.com/1/cards/{id}"

    headers = {
        "Accept": "application/json"
    }
    query = {
                'key': os.environ.get('TrelloAPI'),
                'token': os.environ.get('TrelloToken'),
                'closed': 'true',
                'id': id
    }
    return requests.put(url,headers=headers,data=query)