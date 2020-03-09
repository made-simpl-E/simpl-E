import ply.lex as lex
from ply.lex import TOKEN

import tokens


class SimpleLexer(object):

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=tokens, **kwargs)

    def lex(self, data):
        self.lexer.input(data)
        for tok in self.lexer:
            print(tok)



