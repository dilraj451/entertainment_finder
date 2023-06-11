import PySimpleGUI as sg
from datetime import datetime
from API_response import parse_response, get_ratings, movie_url, base_params

def receive_search():
    """Receieves user input via PySimpleGUI window

    Returns:
        event (str): command to be executed
        values (dict): search parameters defined by user
    """
    # Set window colour
    sg.theme('SandyBeach')     
    
    # Set window features
    title = 'Entertainment Finder'
    box_size = (30, 1)
    text_font = ('Times', 14)

    # Options for year input
    current_year = datetime.now().year
    years = [i for i in range(current_year - 100, current_year + 1)]
    years.append('---')

    # Options for category input
    types = ['movie', 'tv Series']

    # Define window layout
    layout = [
        [
            sg.Text('Title (*)', size = box_size, font=text_font), 
            sg.InputText(key='-TITLE-', font=text_font)
            ],
        [
            sg.Text('Year', size = box_size, font=text_font),
            sg.OptionMenu(years, default_value='---', key='-YEAR-')
            ],
        [
            sg.Text('Category', size = box_size, font=text_font),
            sg.OptionMenu(types, default_value='---', key='-CATEGORY-')
            ],
        [sg.Text('* required field', size = box_size, font=text_font)],
        [sg.Button('Search'), sg.Button('Exit')]
    ]

    # Open window
    window = sg.Window(title, layout)

    # Accept user input only when title field is filled and searched for
    while True:
        event, params = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED or (event == 'Search' and params['-TITLE-'] != ''):
            break
    window.close()

    return event, params

def execute_search(event, params):
    """Executes entertainment search based on prior user defined values

    Args:
        event (str): user's command
        params (dict): user's search parameters

    Returns:
        results (list): parsed API GET response from search
    """
    if event == 'Search':

        # Add year input to API parameters
        if not params['-YEAR-'] == '---':
            base_params['year'] = int(params['-YEAR-'])

        # Add category input to parameters
        if not params['-CATEGORY-'] == '---':
            base_params['titleType'] = params['-CATEGORY-'].replace(' ', '')

        # Obtain API GET results
        results = get_ratings(movie_url, params['-TITLE-'], base_params)
    
        return results
    
def selector(title: str, col: list):
    """Obtain dictionary corresponding to title

    Args:
        title (str): title being searched for
        col (list): data collection of all titles

    Returns:
        entry (dict): dictionary linked to title
    """
    try:
        for entry in col:
            if title == entry['title']:
                return entry
    except TypeError:
        print('Invalid data type(s) for function arguement(s)')
    except KeyError:
        print('Title key does not exist in data set - amend this!')
        