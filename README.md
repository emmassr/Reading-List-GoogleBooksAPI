# Creating a reading list using GoogleBooks API

**Instructions for running the script:**

(Important note: The API key in this application is stored as an environment variable. User can obtain their own API key [here](https://developers.google.com/books/docs/v1/using#APIKey), where they will be instructed on how to generate their own key for the GoogleBooks API).

On the command line the following command should be entered to run the application:

**python **main**.py**


Expectation:
1) It should prompt the user to enter what they would like to search for. Example: Dan Brown

2) It should return a list of 5 results matching the search query with the title, author and publisher (as set in the API parameters).

                        title              author       publisher
              1    The Lost Symbol       [Dan Brown]  Random House
              2    Origin                [Dan Brown]  Random House
              3  Angels and Demons       [Dan Brown]  Random House
              4  Deception Point         [Dan Brown]  Pocket Books
              5  Robert Langdon Omnibus  [Dan Brown]  Random House

3) It should then ask user to make a selection by entering the index (row number) of the book title/author/publisher from the result list and if they would like to add it to their reading list.Example: 2 (if the user wants to select:  Origin [Dan Brown]  Random House)

4) The user will be asked if they would like to search again.

5) If the user continues to search again steps 1 to 4 takes place.

6) If the user no longer wants to search again the script will display the current reading list before exiting the program.
