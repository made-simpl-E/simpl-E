from lexer import SimpleLexer


if __name__ == '__main__':
    lexer = SimpleLexer()
    data = '''one
    one + two
    # hellp
    (two * three)
    '''
    lexer.lex(data)

