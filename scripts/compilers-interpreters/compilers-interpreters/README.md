# Mini Compiler

This is a simple compiler built in Python. It compiles code written in a made-up language, which we'll call 'MiniLang', into Python code. 

## What it does

This compiler can interpret simple 'MiniLang' programs. The syntax for 'MiniLang' is as follows:

- Print a statement: `print ("Hello, World!")`
- Declare a variable: `var x = 5`
- Simple arithmetic: `var y = x + 3`
- If statement: `if (x > y): print ("x is greater")`

## How it works

The compiler works in two stages:

1. Lexical Analysis: This is where the source code is converted into tokens.
2. Parsing: The tokens are then parsed and interpreted.

## How to run

Make sure you have Python installed on your machine. Then, you can run the compiler with the following command: