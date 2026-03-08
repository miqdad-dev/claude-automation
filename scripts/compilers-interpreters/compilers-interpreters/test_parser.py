import unittest
from lexer import Lexer
from parser import Parser

class TestParser(unittest.TestCase):
    def test_parse_print_statement(self):
        lexer = Lexer("print Hello;")
        parser = Parser(lexer)
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [["PRINT", "print"], ["IDENTIFIER", "Hello"], ["STATEMENT_END", ";"]])
        
if __name__ == '__main__':
    unittest.main()