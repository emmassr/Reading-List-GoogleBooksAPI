import requests
import pprint

class GoogleBooks():

    def get_search_result(self, search):
        response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={search}&fields=items(volumeInfo(title, authors, publisher))&maxResults=1&key=")
        pprint.pprint(response)
        return response.json()["items"]
