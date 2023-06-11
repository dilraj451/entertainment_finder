from API_response import get_response, parse_response, get_ratings, base_params

correct_URL = "https://moviesdatabase.p.rapidapi.com/titles/search/title/"
false_URL = "https://moviesdatabase.rapidapi.com/titles"

def test_get_response():
    
    # Check response object returns correct output for correct URL
    response = get_response(correct_URL, 'batman', base_params)
    assert response.status_code == 200
    
    # Check for no response for invalid URL
    false_res = get_response(false_URL, 'batman', base_params)
    assert false_res is None
    
    # Check for no response for invalid search variable datatype
    false_name = get_response(false_URL, 0, base_params)
    assert false_name is None

def test_parse_response():
   
    # Check valid search parameters yields correct return (list)
    base_params['year'] = 2022
    data = parse_response(correct_URL, 'batman', base_params)
    
    assert type(data) is list
    assert list(data[0]) == ['title', 'year', 'category', 'id', 'image']
    assert len(data) > 0

    # Check invalid parameters yields none
    false_data = parse_response(correct_URL, 'khuhajsh', base_params)
    assert false_data is None

def test_get_ratings():
    
    # Check ratings data appended to data collection
    col = get_ratings(correct_URL, 'batman', base_params)
    assert type(col) is list
    assert list(col[0])[-1] is 'rating'
    assert type(col[0]['rating']) is str