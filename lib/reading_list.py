import numpy as np
import requests
import pprint
import json
import pandas as pd
import os



class GoogleBooks():

    def __init__(self):
        self.row_list = []


    def get_search_result(self, user_input, maxResults):

        response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={user_input}&fields=items(volumeInfo(title, authors, publisher))&maxResults={maxResults}&key={os.environ['GOOGLE_BOOKS_API']}")
        response_text = response.json()
        return response_text

    def converts_json_response_to_list(self, response_text):
        vinfo = [v['volumeInfo'] for v in response_text["items"]]
        return vinfo


    def store_list_in_dataframe(self,vinfo):
        df = pd.DataFrame(vinfo, index =[1, 2, 3, 4, 5])
        return df

    def displays_dataframe(self, df):
        display_book_list = df
        print (display_book_list)
        return display_book_list


    def get_user_selection(self, df):

        user_selection = input("Please select a book title you want to add to your reading list, your entry must match the text case:")
        book_selected = df['title'] == user_selection # add that row in the data frame to a list
        if book_selected.any():
            selected_book = df[book_selected]
            # print(selected_book)
            # print(type(selected_book))
            print("You have chosen:")
            return selected_book
        else:
            print("Sorry there was no match found in the list. Check your entry for spelling errors or if it is in the correct case and select again. ")
        return self.get_user_selection(df)

    def adds_selection_to_reading_list(self, selected_book):
        if selected_book is None:
            return self.row_list
        for index, rows in selected_book.iterrows():
            my_list = [rows.title, rows.authors, rows.publisher]
        self.row_list.append(my_list)
        self.display_update_reading_list()
        return self.row_list


    def asks_user_to_search_again(self):
        search_again = input("Would you like to search for another author? Enter y for Yes and n for No:")
        new_search = None
        if search_again == 'y':
            new_search = self.get_search_result(input("Please enter your new author search here:"), 5)
            json_response_new = self.converts_json_response_to_list((new_search))
            new_dataframe = self.store_list_in_dataframe(json_response_new)
            print(new_dataframe)
            new_book_selection = self.get_user_selection(new_dataframe)
            reading_list = self.adds_selection_to_reading_list(new_book_selection)
            # print(reading_list)  # call method instead
            self.asks_user_to_search_again()

        else:
            print('This is your current reading list:')
            self.display_update_reading_list()
            print("Happy Reading!")

    def display_update_reading_list(self):
        for item in self.row_list:
            print("-", item[0], item[1], item[2])


if __name__ == "__main__":
    googlebooks = GoogleBooks()
    user_input = input("Which author would you like to search for?:")
    search_result = googlebooks.get_search_result(user_input, 5)
    json_response = googlebooks.converts_json_response_to_list(search_result)
    book_list = googlebooks.store_list_in_dataframe(json_response)
    display_book_list = googlebooks.displays_dataframe(book_list)
    book_to_read = googlebooks.get_user_selection(display_book_list)
    reading_list = googlebooks.adds_selection_to_reading_list(book_to_read)
    search_for_new_book = googlebooks.asks_user_to_search_again()
