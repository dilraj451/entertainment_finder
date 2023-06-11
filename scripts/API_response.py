import requests
import os

base_url = "https://moviesdatabase.p.rapidapi.com/titles/"
movie_url = base_url + "search/title/"
key = os.environ.get('API_KEY')
host_name = "moviesdatabase.p.rapidapi.com"

headers = {"X-RapidAPI-Key": key, "X-RapidAPI-Host": host_name}
base_params = {'exact': False}

def get_response(url: str, name: str, params: dict):
    """Retrieves response from API GET request

    Args:
        url (str): API's URL
        name (str): name of movie / show being searched for
        params (dict): API GET call parameters

    Raises:
        ce: ConnectionError - if invalid URL input or no Internet connection occurs

    Returns:
        response: Response object containing data from GET request
    """
    # search parameters - can be added to
    
    try:
        # Make GET request and return response
        response = requests.get(url + name.replace(' ', '%20'),
                                headers=headers,
                                params=params)
        return response
    
    # Catch requests connection error
    except requests.exceptions.ConnectionError:
        print("Page not found")
    except AttributeError:
        print("Invalid data type input as title")
    

def parse_response(url: str, name: str, params: dict):
    """Extracts title, year, and category from response data

    Args:
        url (str): API's URL
        name (str): name of movie / show being searched for

    Returns:
        collection (list): list of dictionaries containing parsed data for each entry
    """
    # Make GET request and parse if entries present
    response = get_response(url, name, params)
    if response:
        all_data = response.json()
        if all_data['entries'] != 0:

            data = all_data['results']
            collection = []

            # Store entry's title, year, and category in dictionary and append to returned collection
            for entry in data:
                info = {}
                info['title'] = entry['originalTitleText']['text']
                info['year'] = entry['releaseYear']['year']
                info['category'] = entry['titleType']['text']
                info['id'] = entry['id']
                if entry['primaryImage']:
                    info['image'] = entry['primaryImage']['url']
                else:
                    info['image'] = None
                collection.append(info)

            return collection
    
def get_ratings(url: str, name: str, params: dict):
    """Appends IMDb ratings data to each entry

    Args:
        url (str): _description_
        name (str): _description_
        params (dict): _description_


    Returns:
        _type_: _description_
    """
    # Obtains and parses data from API GET request
    col = parse_response(url, name, params)

    # For each entry, rating is searched for and appended to dataset
    if col:
        for show in col:
            try:
                response = requests.get(base_url + show['id'] + '/ratings', headers=headers).json()['results']
            # Catch requests connection error
            except requests.exceptions.ConnectionError as ce:
                print("Page not found")
                raise ce
            if response is None:
                show['rating'] = 'N/A'
            else:
                show['rating'] = str(response['averageRating'])
                
        return col

def load_images(url: str):
    pass

if __name__ == '__main__':
    print(get_response(movie_url, 'batman').json()['results'][4])