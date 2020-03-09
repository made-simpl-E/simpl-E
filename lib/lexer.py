import ply.lex as lex
from ply.lex import TOKEN

from tokens import tokens, reserved


class SimpleLexer(object):
    tokens = tokens

    reserved = reserved

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def lex(self, data):
        self.lexer.input(data)
        for tok in self.lexer:
            print(tok)

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'\/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_LSQBRACE = r'\['
    t_RSQBRACE = r'\]'
    t_PERIOD = r'\.'
    t_COMMA = r','
    t_COLON = r':'

    t_ignore = r' '
    t_ignore_COMMENT = r'\#.*'

    @TOKEN(r'\d+')
    def t_NUMBER(self, t):
        t.value = int(t.value)
        return t

    @TOKEN(r'[a-zA-Z_][a-zA-Z_0-9]*')
    def t_ID(self, t):
        t.type = reserved.get(t.value, 'ID')
        return t

    @TOKEN(r'\n+')
    def t_newline(self, t):
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Illegal character: {t.value[0]}")
        t.lexer.skip(1)

