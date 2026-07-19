# Automated Bot

This project consists of a bot that automates a Google search for a term. It uses Selenium for automation and Python for scripting.

## How it works

The bot opens a new browser window, navigates to Google's main page, enters a search term into the search box, and then prints the first search result.

## How to run

1. Install Python 3.

2. Install selenium: `pip install selenium`.

3. Download the ChromeDriver from the following link: https://sites.google.com/a/chromium.org/chromedriver/downloads. Extract it and save the `chromedriver` file in the same directory as this script.

4. Run the script: `python automated_bot.py`.

## Example usage

To search for "Python", run `python automated_bot.py`.

## Architecture & Tradeoffs

This bot uses Selenium, which is a powerful tool for controlling a web browser through the program. It's perfect for automation of complex web tasks. The drawback is that it is somewhat slower than an API or a direct HTTP request, and it requires a fair amount of resources (as it needs to run a full-fledged web browser).

The script is fairly simple and does not include error handling. It assumes that the elements it interacts with (the search box and the first result) will always be present on the page.