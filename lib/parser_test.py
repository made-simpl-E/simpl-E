from parser import SimpleParser
from lexer import SimpleLexer


if __name__ == '__main__':
    lexer = SimpleLexer()
    parser = SimpleParser(lexer)

    parser.test()

