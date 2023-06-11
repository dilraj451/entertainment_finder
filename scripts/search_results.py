from search_functions import selector
from image_loader import loader, resize
from get_video import scraper
import PySimpleGUI as sg


def output_results(search_res, params):
    """GUI output displaying entertainment search results and details

    Args:
        search_res (list): list of dictionaries containing entertainment details
        params (dict): user's search parameters
    """
    if search_res and params:

    
        # Obtain list of titles for option display
        gui_list = []
        for res in search_res:
            gui_list.append(res['title'])

        # Define window characteristics
        title = "Search results"
        list_size = (40, 20)
        detail_size = (40, 1)
        image_size = (550, 550)
        options_font = ('Times', 14)
        solo_font = ('Times', 16)

        # Define search result column layout
        results_column = [
            [sg.Text(f"Results matching '{params['-TITLE-']}'", font=options_font)],
            [sg.Listbox(
                values=gui_list, enable_events=True, size=list_size, key="-RESULT LIST-", font=options_font)],
            [sg.Button('Watch Now')]
        ]

        # Define title details section layout
        details = [
            [sg.Text(size=detail_size, key="-TITLE OUT-", font=solo_font)],
            [sg.Text(size=detail_size, key="-DETAILS OUT-", font=solo_font)],
            [sg.Image(data=None, key='-IMG-')]
        ]


        # Define overall window layout
        layout = [
            [
                sg.Column(results_column),
                sg.VSeperator(),
                sg.Column(details)
            ]
        ]

        # Open window
        window = sg.Window(title, layout)

        while True:
            # Scan user actions and terminate if quit or window closed
            event, values = window.read()
            if event == 'Exit' or event == sg.WIN_CLOSED:
                break
            

            # Open title details when clicked
            if event == "-RESULT LIST-":
                # Read title selected and find corresponding data
                title = values["-RESULT LIST-"][0]
                selected = selector(title, search_res)
                # Output title data and image to window
                window['-TITLE OUT-'].update(f"{title} ({selected['year']})")
                window['-DETAILS OUT-'].update(f"{selected['category']}, IMDb: {selected['rating']}")
                window['-IMG-'].update(data=resize(loader(selected['image']), image_size))

            if event == 'Watch Now':
                try:
                    scraper(title, selected['year'])
                except UnboundLocalError:
                    print("No title selected!")


        # Close window when terminated
        window.close()

        return True
    


