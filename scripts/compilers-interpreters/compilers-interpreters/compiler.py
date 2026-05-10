import sys
import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
        tokens = []
        source_code = self.source_code.split()
        source_index = 0

        while source_index < len(source_code):
            word = source_code[source_index]

            if word == "var":
                tokens.append(Token("VAR_DECLARATION", word))
            
            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                tokens.append(Token("IDENTIFIER", word))

            elif re.match('[0-9]', word):
                tokens.append(Token("INTEGER", word))

            elif word in "=*/+-":
                tokens.append(Token("OPERATOR", word))

            elif word == ";":
                tokens.append(Token("STATEMENT_END", word))

            source_index += 1

        return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0

    def parse(self):
        while self.token_index < len(self.tokens):
            token = self.tokens[self.token_index]

            if token.type == "VAR_DECLARATION":
                self.declare_variable()

            self.token_index += 1

    def declare_variable(self):
        identifier = self.tokens[self.token_index + 1]
        operator = self.tokens[self.token_index + 2]
        integer = self.tokens[self.token_index + 3]

        print(f"{identifier.value} {operator.value} {integer.value}")

def main():
    with open(sys.argv[1], 'r') as source_code:
        lexer = Lexer(source_code.read())
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        parser.parse()

if __name__ == "__main__":
    main()