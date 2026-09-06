# Data Engineering Mini Project

## Description

This is a mini-hard project in the field of data engineering. The project reads a CSV file, cleans the data and calculates the average age.

## How it Works

The project is written in Python and uses the pandas library for data manipulation and numpy for handling NaN values. 

The `app.py` script contains the following functions:
- `load_data()`: reads a CSV file and returns a pandas DataFrame
- `clean_data()`: replaces empty strings with NaN, then drops rows with NaN values
- `get_average_age()`: calculates and returns the average age

## How to Run

1. Install the required dependencies: