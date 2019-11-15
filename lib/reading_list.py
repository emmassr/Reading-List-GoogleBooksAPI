import requests
import pprint
import json
import pandas as pd






class GoogleBooks():

    # def asks_user_input(self):
    #     user_input = input("What book would you like to search for?")
    #     # result = get_search_result(self, search)
    #     return user_input

    def get_search_result(self, user_input, maxResults):
        # user_input = input("What book would you like to search for?")
        print("check1")
        response = requests.get(
            f"https://www.googleapis.com/books/v1/volumes?q={user_input}&fields=items(volumeInfo(title, authors, publisher))&maxResults={maxResults}&key=AIzaSyBj5vVsFkryyWruvCwbZnqREizNtw3Twdg")
        response_text = response.json()
        pp = pprint.PrettyPrinter()
        pp.pprint(response_text["items"])
        print("checka")
        vinfo = [v['volumeInfo'] for v in response_text["items"]]
        pp.pprint(vinfo)
        print("checkb")
        df = pd.DataFrame(vinfo)
        print(df)
        return pd.DataFrame(vinfo)

        # return vinifo
        # print(response_text)
        # pp = pprint.PrettyPrinter()
        # pp.pprint(response)
        # pprint.pprint(response)
        # pprint.pprint(response)
        # return response_text["items"]
    print(2.5)
    def gets_list_of_books(self, response_text):
        

    # #display the results
    # #store json results in an array
    # #promt user to pick something from json array to put in new array called reading readingList
    # #prompt user if they want to search again
    # #if yes go back to get search result function
    # #if no then display end of search
    #


if __name__ == "__main__":
    googlebooks = GoogleBooks()
    user_input = input("What book would you like to search for?")

    value = googlebooks.get_search_result(user_input, 5)

    # googlebooks.gets_list_of_books(value)
