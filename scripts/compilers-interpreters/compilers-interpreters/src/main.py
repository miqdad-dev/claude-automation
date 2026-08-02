import rply

lexer = rply.LexerGenerator()

# Define our tokens
lexer.add('NUMBER', r'\d+')
lexer.add('PLUS', r'\+')
lexer.add('MINUS', r'\-')
lexer.add('OPEN_PARENS', r'\(')
lexer.add('CLOSE_PARENS', r'\)')

lexer.ignore('\s+')

lexer = lexer.build()

for token in lexer.lex('1 + 1 - (2 + 3)'):
    print(token)