import numpy as np
import requests
import pprint
import json
import pandas as pd
import os

class GoogleBooks():


    def get_search_result(self, user_input, maxResults):

        response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={user_input}&fields=items(volumeInfo(title, authors, publisher))&maxResults={maxResults}&key={os.environ['GOOGLE_BOOKS_API']}")
        response_text = response.json()
        vinfo = [v['volumeInfo'] for v in response_text["items"]]
        return vinfo


    def store_search_result_in_dataframe(self,vinfo):
        df = pd.DataFrame(vinfo, index =[1, 2, 3, 4, 5])
        return df

    def displays_dataframe(self, df):
        display_book_list = df
        print (display_book_list)
        return display_book_list


    def get_user_selection(self, df):

        user_selection = input("Please select a book title you want to add to your reading list, your entry must match the text case:")
        book_selected = df['title'] == user_selection
        while book_selected.any():
            selected_book = df[book_selected]
            print(type(selected_book))
            return selected_book
        else:
            print("Sorry there was no match found in the list. Check your entry for spelling errors or if it is in the correct case and select again. ")
        return self.get_user_selection(df)
        print("is this working")

    def adds_selection_to_reading_list(self,selected_book):
        row_list = []
        print(type(selected_book))
        # Iterate over each row
        for index, rows in selected_book.iterrows():
        # Create list for the current row
            my_list = [rows.title, rows.authors, rows.publisher]
        # append the list to the final list
        row_list.append(my_list)
        return row_list


    def asks_user_to_search_again(self):
        search_again = input("Would you like to search again? Enter y for Yes and n for No:")
        new_search = None
        if search_again == 'y':
            new_search = self.get_search_result(input("Please enter your new search:"), 5)
            new_dataframe = self.store_search_result_in_dataframe(new_search)
            print(new_dataframe)
            new_book_selection = self.get_user_selection(new_dataframe)
            reading_list = self.adds_selection_to_reading_list(new_book_selection)
            print(reading_list)
            return reading_list

        # for user_wants_search_again in search_again:
        # if user_wants_search_again:
        #     new_book_search = self.get_search_result(input("Please enter a new book you would like to search for:"), 5)
        #     book_dataframe = pd.DataFrame(new_book_search, index =[1, 2, 3, 4, 5])
        #     print(book_dataframe)
        #     new_list = row_list.append(book_dataframe)
        #     print("what happening now?")
        #     print(new_list)
        #     # new_book_selection = self.get_user_selection(book_dataframe)
        #     # self.adds_selection_to_reading_list(new_book_selection)
        #
        # # row_list.append(new_book_selection)
            # print(new_book_selection)
            # self.adds_selection_to_reading_list(new_book_selection)
        else:
            print("Happy Reading!")





if __name__ == "__main__":
    googlebooks = GoogleBooks()
    user_input = input("What book would you like to search for?")
    search_result = googlebooks.get_search_result(user_input, 5)
    book_list = googlebooks.store_search_result_in_dataframe(search_result)
    display_book_list = googlebooks.displays_dataframe(book_list)
    book_to_read = googlebooks.get_user_selection(display_book_list)
    # googlebooks.get_user_input(value)
    reading_list = googlebooks.adds_selection_to_reading_list(book_to_read)
    # print(reading_list)
    search_for_new_book = googlebooks.asks_user_to_search_again()
