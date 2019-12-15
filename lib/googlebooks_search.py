import requests
import pandas as pd
import os

def get_search_result(user_input, maxResults):

    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={user_input}&fields=items(volumeInfo(title, authors, publisher))&maxResults={maxResults}&key={os.environ['GOOGLE_BOOKS_API']}")
    response_text = response.json()
    return response_text

def converts_json_response_to_list(response_text):
    json_response_to_list = [v['volumeInfo'] for v in response_text["items"]]
    return json_response_to_list

def store_list_in_dataframe(json_response_to_list):
    json_to_dataframe = pd.DataFrame(json_response_to_list, index =[1, 2, 3, 4, 5])
    pd.set_option("display.colheader_justify", "left")
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)
    print(json_to_dataframe)
    return json_to_dataframe
