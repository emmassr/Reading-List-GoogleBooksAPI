import unittest
import pandas as pd
import pandas.util.testing
from lib import googlebooks_search


maxDiff = None
class TestGoogleBooks(unittest.TestCase):

    def test_gets_results_when_search_query_entered(self):
        book_search = googlebooks_search.get_search_result("Dan Brown", 1)
        self.assertEqual(book_search, {'items': [{'volumeInfo':{'title': 'The Lost Symbol', 'authors': ['Dan Brown'], 'publisher': 'Random House'}}]})

    def test_gets_more_than_one_result_query_entered(self):
        book_search = googlebooks_search.get_search_result("Dan Brown", 2)
        self.assertEqual(book_search, {'items': [{'volumeInfo': {'title': 'The Lost Symbol', 'authors': ['Dan Brown'], 'publisher': 'Random House'}}, {'volumeInfo': {'title': 'Origin', 'authors': ['Dan Brown'], 'publisher': 'Random House'}}]} )

    def test_gets_json_response_in_list(self):
        response_text = {'items': [{'volumeInfo': {'title': 'The Lost Symbol', 'authors': ['Dan Brown'], 'publisher': 'Random House'}}, {'volumeInfo': {'title': 'Origin', 'authors': ['Dan Brown'], 'publisher': 'Random House'}}, {'volumeInfo': {'title': 'Angels and Demons', 'authors': ['Dan Brown'], 'publisher': 'Random House'}}, {'volumeInfo': {'title': 'Robert Langdon Omnibus', 'authors': ['Dan Brown'], 'publisher': 'Random House'}}, {'volumeInfo': {'title': 'Angels & Demons', 'authors': ['Dan Brown'], 'publisher': 'Simon and Schuster'}}]}
        response_list = googlebooks_search.converts_json_response_to_list(response_text )
        self.assertEqual(response_list, [{'title': 'The Lost Symbol',
                                                  'authors': ['Dan Brown'],
                                                  'publisher': 'Random House'},
                                        {'title': 'Origin',
                                                  'authors': ['Dan Brown'],
                                                  'publisher': 'Random House'},
                                        {'title': 'Angels and Demons',
                                                  'authors': ['Dan Brown'],
                                                  'publisher': 'Random House'},
                                        {'title': 'Robert Langdon Omnibus',
                                                  'authors': ['Dan Brown'],
                                                  'publisher': 'Random House'},
                                        {'title': 'Angels & Demons',
                                                  'authors': ['Dan Brown'],
                                                  'publisher': 'Simon and Schuster'}])


if __name__ == '__main__':
    unittest.main()
