from display_prompts import DisplayEnum
import googlebooks_search
import user_selection

row_list = []

def adds_selection_to_reading_list(selected_book):
    if selected_book is None:
        row_list
    for index, rows in selected_book.iterrows():
        list_to_add = [rows.title, rows.authors, rows.publisher]
        row_list.append(list_to_add)
    print('Your selection was: ')
    display_update_reading_list()
    return row_list

def asks_user_to_search_again():
    search_again = input("Would you like to search again? Enter y for Yes and n for No:")
    new_search = None
    if search_again == 'y':
        new_search = googlebooks_search.get_search_result(input(DisplayEnum.SEARCH_QUERY.value), 5)
        json_response_new = googlebooks_search.converts_json_response_to_list(new_search)
        new_dataframe = googlebooks_search.store_list_in_dataframe(json_response_new)
        print(new_dataframe)
        new_book_selection = user_selection.get_user_selection(new_dataframe)
        print('This is your current reading list:')
        adds_selection_to_reading_list(new_book_selection)
        asks_user_to_search_again()
    else:
        print('This is your current reading list:')
        display_update_reading_list()
        print("Happy Reading!")

def display_update_reading_list():
    for item in row_list:
        print(item[0], item[1], item[2])
