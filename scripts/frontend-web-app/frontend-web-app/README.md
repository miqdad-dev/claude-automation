# Frontend Web App

This application is a simple frontend web app that takes an input and queries an API to find related Wikipedia articles. It handles concurrency using Promises and uses the Fetch API.

## How It Works

The app uses the Fetch API to query the Wikipedia API. The Fetch API returns a Promise that is resolved to the Response to that request, whether it is successful or not. The app then uses the `.json()` method of the Response object to read the body content as JSON.

## How To Run

1. Clone the repository.
2. Open the index.html file in a web browser.

## Example Usage

1. Enter a search term into the input box.
2. Click the 'Search' button.
3. The app will display a list of related Wikipedia articles.

## Architecture & Tradeoffs

The app is designed as a single-page application (SPA) for simplicity. This means that it does not require a server to run, but it also means that it is entirely client-side and cannot handle server-side logic.

The app uses the Fetch API instead of the older XMLHttpRequest for making HTTP requests. This has the advantage of being more modern and flexible, but it may not be supported in all browsers.

The app uses Promises to handle concurrency. This allows it to perform multiple requests at once and handle them in whichever order they complete, but it also means that the app may not work as expected if the requests fail.