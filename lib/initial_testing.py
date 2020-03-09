from lexer import SimpleLexer


data = '''# one
two = one + 43
three = (two + 5) * 24 / 6
list = [0, 1, 2, 3]
dict = {0: 0, 1: 1, 2: 2}

func name(args) {
    return 4 + args
}
'''

if __name__ == '__main__':
    lexer = SimpleLexer()
    lexer.lex(data)

