from get_video import scraper, base_url

def test_scraper():
    title = 'batman'
    year = 1989

    search_link = scraper(title, year)
    assert search_link == base_url + f"batman+1989"

    