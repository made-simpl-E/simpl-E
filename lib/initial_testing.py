from lexer import SimpleLexer


data = '''one
one + two
# hellp
(two * three)
'''

if __name__ == '__main__':
    lexer = SimpleLexer()
    lexer.lex(data)

