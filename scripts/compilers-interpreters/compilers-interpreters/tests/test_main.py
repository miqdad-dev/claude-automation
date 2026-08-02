import unittest
import rply
from src.main import lexer

class TestLexer(unittest.TestCase):

    def test_number(self):
        token = next(lexer.lex('123'))
        self.assertEqual(token.gettokentype(), 'NUMBER')
        self.assertEqual(token.getstr(), '123')

    def test_plus(self):
        token = next(lexer.lex('+'))
        self.assertEqual(token.gettokentype(), 'PLUS')
        self.assertEqual(token.getstr(), '+')

    def test_minus(self):
        token = next(lexer.lex('-'))
        self.assertEqual(token.gettokentype(), 'MINUS')
        self.assertEqual(token.getstr(), '-')

    def test_open_parens(self):
        token = next(lexer.lex('('))
        self.assertEqual(token.gettokentype(), 'OPEN_PARENS')
        self.assertEqual(token.getstr(), '(')

    def test_close_parens(self):
        token = next(lexer.lex(')'))
        self.assertEqual(token.gettokentype(), 'CLOSE_PARENS')
        self.assertEqual(token.getstr(), ')')

if __name__ == '__main__':
    unittest.main()