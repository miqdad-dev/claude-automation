import unittest
from compiler import Lexer, Parser, Token

class TestCompiler(unittest.TestCase):
    def test_tokenize(self):
        lexer = Lexer("var x = 5")
        tokens = lexer.tokenize()
        self.assertEqual(tokens[0].type, "VAR_DECLARATION")
        self.assertEqual(tokens[0].value, "var")
        self.assertEqual(tokens[1].type, "IDENTIFIER")
        self.assertEqual(tokens[1].value, "x")
        self.assertEqual(tokens[2].type, "OPERATOR")
        self.assertEqual(tokens[2].value, "=")
        self.assertEqual(tokens[3].type, "INTEGER")
        self.assertEqual(tokens[3].value, "5")

    def test_parse(self):
        tokens = [Token("VAR_DECLARATION", "var"), Token("IDENTIFIER", "x"), Token("OPERATOR", "="), Token("INTEGER", "5")]
        parser = Parser(tokens)
        parser.parse()

if __name__ == "__main__":
    unittest.main()