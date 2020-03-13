from os.path import join, abspath, dirname
from sys import path
path.insert(0, join(dirname(dirname(abspath(__file__))), 'interpreter'))

from simple_lexer import SimpleLexer


if __name__ == '__main__':
    code = '''first = 1
    second = 2.32
    third = first + second
    fourth = second * third / first
    fifth = fourth - first'''
    lexer = SimpleLexer(test_mode=True)
    output = lexer.test(code)
    print(output)

