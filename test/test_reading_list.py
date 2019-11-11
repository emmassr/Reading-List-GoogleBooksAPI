from lib.reading_list import GoogleBooks
import requests



def test_gets_results_when_search_query_entered():
    books = GoogleBooks()
    search = "The Da Vinci Code Travel Journal"
    assert books.get_search_result(search) == [{'volumeInfo': {'title': 'The Da Vinci Code Travel Journal', 'authors': ['Dan Brown'], 'publisher': 'Clarkson Potter'}}]

def test_gets_results_when_different_search_query_entered():
    books = GoogleBooks()
    search = "Lord of the Rings"
    assert books.get_search_result(search) == [{'volumeInfo': {'title': 'The Fellowship of the Ring', 'authors': ['John Ronald Reuel Tolkien', 'Alan Lee'], 'publisher': 'HarperCollins UK'}}]
