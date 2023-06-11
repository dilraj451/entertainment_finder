<h1>Entertainment Finder</h1>

<h3>Functionality</h3>
Combination of GUI and CLI for user to search for and watch movies and/or TV shows from an extensive catalogue.

The user is able to select the title (compulsory field), release year, and category of the entertainment; from the search result list, they can select to view further details of each and press 'Watch Now', which opens the corresponding YouTube search page for the mvoie / show.

<h3>Motivation</h3>
My personal motivation for this project was to consolidate my understanding of Python fundamentals, utilizing RESTful APIs, as well as learning how to incoroporate GUI via the PySimpleGUI module.

<h3>Operating Instructions</h3>
Several third-party modules were applied for this project - see 'requirements.txt'.

An API key is required to access moviesdatabase.p.rapidapi.com, the API used in this project. Save the API key as an environment variable named 'API_KEY' in a virtual environment to be accessed in the 'API_response.py' script.

Run the 'main.py' script from the scripts folder to launch the program.

All testing scripts are .py files with file names starting with 'test_'. Pytest framework was used to execute the tests