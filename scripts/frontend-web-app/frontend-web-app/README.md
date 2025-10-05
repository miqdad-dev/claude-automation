# Frontend Web App

This is a simple e-commerce shopping cart feature. It allows users to add items to the cart and view them. The shopping cart updates in real-time when items are added.

## How it works

The app uses JavaScript events and DOM manipulation to update the cart in real-time when an item is added. 

## How to run 

1. Clone the repository
2. Navigate to the root directory (`frontend-web-app`)
3. Run `npm install` to install dependencies
4. Run `npm start` to start the app
5. Visit `http://localhost:3000` in your browser

## Example usage

Click on the 'Add to cart' button next to an item to add it to the cart. The cart contents are displayed below.

## Architecture & Tradeoffs

The app is built with simplicity in mind, so it only includes a basic functionality. There is no backend or database, and the cart contents do not persist if the page is refreshed. 

As a trade-off for its simplicity, the app does not support multiple quantities of the same item, removing items from the cart, or checkout functionality. These could be added in a more full-featured version of the app.