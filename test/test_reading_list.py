from lib.reading_list import GoogleBooks
from pandas.util.testing import assert_frame_equal


import requests
import unittest


class TestGoogleBooks(unittest.TestCase):

    def test_gets_results_when_search_query_entered(self):
        googlebooks = GoogleBooks()
        book_search = googlebooks.get_search_result("Dan Brown", 1)
        self.assertEqual(book_search,[{'title': 'The Lost Symbol', 'authors': ['Dan Brown'],'publisher': 'Random House'}])

    def test_gets_more_than_one_result_query_entered(self):
        googlebooks = GoogleBooks()
        book_search = googlebooks.get_search_result("Dan Brown", 2)
        self.assertEqual(book_search,[{'title': 'The Lost Symbol', 'authors': ['Dan Brown'],'publisher': 'Random House'}, {'title': 'Origin','authors': ['Dan Brown'], 'publisher': 'Random House'}])


    def test_displays_results_in_dataframe(self):
        googlebooks= GoogleBooks()
        vinfo = googlebooks.get_search_result("Dan Brown", 5)
        check_book_list = googlebooks.store_search_result_in_dataframe(vinfo)
        check = check_book_list.applymap(lambda x: x == 'Dan Brown').any().any()
        self.assertIn(check, check_book_list, 'title')



if __name__ == '__main__':
    unittest.main()
