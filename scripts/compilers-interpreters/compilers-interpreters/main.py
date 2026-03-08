from lexer import Lexer
from parser import Parser

def main():
    content = ""
    
    with open('test.txt', 'r') as file:
        content = file.read()

    lexer = Lexer(content)
    parser = Parser(lexer)
    parser.parse()

if __name__ == "__main__":
    main()