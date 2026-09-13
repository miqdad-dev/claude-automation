import scraper
from unittest.mock import patch

@patch('scraper.requests.get')
def test_scrape_weather(mock_get):
    # Mock the response from the GET request
    mock_get.return_value.content = """
    <section class="forecast">
        <div class="day">
            <span class="date">2022-04-01</span>
            <span class="weather">Sunny</span>
            <span class="temperature">24°C/75°F</span>
        </div>
    </section>
    """

    # Call the function we're testing
    scraper.scrape_weather()

    # Check that the GET request was made to the correct URL
    mock_get.assert_called_with(scraper.URL)