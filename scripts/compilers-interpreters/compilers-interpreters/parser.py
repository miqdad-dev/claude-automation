from lexer import Lexer

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = lexer.tokenize()

    def parse(self):
        i = 0
        while i < len(self.tokens):
            token_type = self.tokens[i][0]
            token_value = self.tokens[i][1]

            if token_type == "IDENTIFIER" and token_value == "var":
                self.parse_variable_declaration(i)
            elif token_type == "IDENTIFIER":
                self.parse_identifier(i)

            i += 1

    def parse_variable_declaration(self, i):
        identifier = self.tokens[i][1]
        value = self.tokens[i+2][1]

        print("Variable Declaration: Name:", identifier, "Value:", value)

    def parse_identifier(self, i):
        print("Identifier:", self.tokens[i][1])