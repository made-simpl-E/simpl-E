from os.path import join, abspath, dirname
from sys import path
path.insert(0, join(dirname(dirname(abspath(__file__))), 'interpreter'))

from simple_parser import SimpleParser
from simple_lexer import SimpleLexer


if __name__ == '__main__':
    lexer = SimpleLexer()
    parser = SimpleParser(lexer)

    parser.test()

