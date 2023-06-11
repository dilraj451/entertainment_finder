from search_functions import receive_search, execute_search
from search_results import output_results

event, params = receive_search()
results = execute_search(event, params)
displayed = output_results(results, params)

# CLI message if no search results found
if displayed is None:
    print("No results for your search")