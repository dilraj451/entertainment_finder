import webbrowser

base_url = "https://www.youtube.com/results?search_query="

def scraper(title: str, year: int):
    """Opens YouTube search page for input movie / TV title

    Args:
        title (str): title of content
        year (int): release year of content

    Returns:
        search_url: URL opened by webbrowser method
    """
    search_url = base_url + f"{title.lower().replace(' ', '+')}+{str(year)}"
    try:
        webbrowser.open_new(search_url)
    except Exception as e:
        print(f"Web Browser Error: {e}")
    else:
        return search_url