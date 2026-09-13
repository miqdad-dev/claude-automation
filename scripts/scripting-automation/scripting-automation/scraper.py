import requests
from bs4 import BeautifulSoup

# URL of the weather website
URL = "http://www.weather.com/some-city"

def scrape_weather():
    # Send a GET request to the website
    response = requests.get(URL)

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the weather forecast section
    forecast_section = soup.find('section', {'class': 'forecast'})

    # Extract the weather information for the next 7 days
    for day in forecast_section.find_all('div', {'class': 'day'}):
        date = day.find('span', {'class': 'date'}).text
        weather = day.find('span', {'class': 'weather'}).text
        temperature = day.find('span', {'class': 'temperature'}).text
        print(f"Date: {date}, Weather: {weather}, Temperature: {temperature}")

if __name__ == "__main__":
    scrape_weather()