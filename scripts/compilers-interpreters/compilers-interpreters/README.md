# Mini Lexer

A mini lexer that can parse arithmetic expressions.

## What it does

This lexer can recognize numbers, plus, minus, open parenthesis and close parenthesis tokens. It is a fundamental part of a compiler or interpreter.

## How it works

This lexer uses regular expressions to match the input string to the correct tokens. For example, the regular expression for a number is `\d+`, which matches one or more digits.

## How to run

1. Clone the repository
2. Navigate to the project's root folder
3. Install the dependencies: `pip install rply`
4. Run the main file: `python src/main.py`
5. Run the tests: `python -m unittest tests/test_main.py`

## Example usage