# Mini Compiler API

## What it does
This API is a mini compiler. It receives a piece of code as input and returns the compiled output.

## How it works
The API is built using Flask and it uses subprocess.run to run the code through the Python interpreter. It only supports Python code for now and the output is returned as a string.

## How to run
1. Set up a Python virtual environment and activate it.
2. Install the dependencies using pip: `pip install -r requirements.txt`.
3. Run the API using Flask: `flask run`.

## Example usage
Send a POST request to the `/compile` endpoint with the following body: