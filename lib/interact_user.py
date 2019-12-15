import googlebooks_search
import user_selection
import reading_list
from display_prompts import DisplayEnum

def interact_with_user():
    user_input = input(DisplayEnum.SEARCH_QUERY.value)
    search_result = googlebooks_search.get_search_result(user_input, 5)
    json_response = googlebooks_search.converts_json_response_to_list(search_result)
    book_list = googlebooks_search.store_list_in_dataframe(json_response)
    book_to_read = user_selection.get_user_selection(book_list)
    reading_list.adds_selection_to_reading_list(book_to_read)
