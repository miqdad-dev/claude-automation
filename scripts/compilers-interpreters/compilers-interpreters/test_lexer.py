import unittest
from lexer import Lexer

class TestLexer(unittest.TestCase):
    def test_tokenize_print_statement(self):
        lexer = Lexer("print Hello;")
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [["PRINT", "print"], ["IDENTIFIER", "Hello"], ["STATEMENT_END", ";"]])
        
if __name__ == '__main__':
    unittest.main()