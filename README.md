# Reading-List-GoogleBooksAPI

**Instructions for running the script:**

On the command line the following command should be entered to run the application:

**python reading_list.py**


Expectation:
1) It should prompt the user to enter the author they would like to search for. Example: Dan Brown

2) It should return a list of 5 results matching the search query with the title, author and publisher (as set in the API parameters).

             title              author       publisher
    1    The Lost Symbol       [Dan Brown]  Random House
    2    Origin                [Dan Brown]  Random House
    3  Angels and Demons       [Dan Brown]  Random House
    4  Deception Point         [Dan Brown]  Pocket Books
    5  Robert Langdon Omnibus  [Dan Brown]  Random House

3)It should then ask user to select a book title from the result list and if they would like to add it to their reading list.The user must enter the book title in the exact sentence case as shown in the results.

4)The user will be asked if they would like to search again.

5) If the user no longer wants to search again the script will display the current reading list before exiting the program.
