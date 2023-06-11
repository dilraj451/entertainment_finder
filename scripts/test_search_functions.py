from search_functions import execute_search, selector
from extra import example_search

def test_execute_search():
    
    cor_params = {'-TITLE-': 'Batman',
                  '-YEAR-': 2022,
                  '-CATEGORY-': '---'}
    
    # Check exit event produces no search
    event = 'Exit'
    no_result = execute_search(event, cor_params)
    assert no_result is None

    # Check search event correctly executes search - verified via previously found data
    event = 'Search'
    cor_result = execute_search(event, cor_params)
    assert cor_result == example_search

def test_selector():

    # Check successful operation of selector
    searching_for = 'Batman 3: Beyond Arkham'
    dataset = selector(searching_for, example_search)
    assert type(dataset) is dict
    assert dataset['title'] == searching_for

    # Check for no return if invalid title input
    invalid_title = 0
    invalid_data = selector(invalid_title, example_search)
    assert invalid_data is None

    # Check for no return if dataset type is invalid
    invalid_dataset = True
    data_wrong = selector(searching_for, invalid_dataset)
    assert data_wrong is None