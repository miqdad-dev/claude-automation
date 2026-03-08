import sys
import re

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []

    def tokenize(self):
        source_code = self.source_code.split('\n')

        source_index = 0

        while source_index < len(source_code):
            
            line = source_code[source_index]

            tokenized = re.split("\s", line)

            for token in tokenized:
                if token == "print":
                    self.tokens.append(["PRINT", token])

                elif re.match("[a-z]", token) or re.match("[A-Z]", token):
                    if token[len(token) - 1] == ";":
                        self.tokens.append(["IDENTIFIER", token[0:len(token) - 1]])
                        self.tokens.append(['STATEMENT_END', ';'])

                elif re.match("[0-9]", token):
                    if token[len(token) - 1] == ";":
                        self.tokens.append(["INTEGER", token[0:len(token) - 1]])
                        self.tokens.append(['STATEMENT_END', ';'])

            source_index += 1

        return self.tokens