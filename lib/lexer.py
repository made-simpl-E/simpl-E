import ply.lex as lex
from ply.lex import TOKEN

from tokens import literals, tokens, reserved, states
from re_strings import *


class SimpleLexer(object):
    literals = literals

    tokens = tokens

    reserved = reserved

    states = states

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.scope_level = 0

    def lex(self, data):
        self.lexer.input(data)
        for tok in self.lexer:
            print(' ' * 4 * self.scope_level + str(tok))

    t_ignore = r' '
    t_MAP_ignore = r' '
    t_ignore_COMMENT = r'\#.*'

    @TOKEN(NUMBER_RE)
    def t_MAP_NUMBER(self, t):
        return self.t_NUMBER(t)

    @TOKEN(NUMBER_RE)
    def t_NUMBER(self, t):
        t.value = int(t.value)
        return t

    @TOKEN('func')
    def t_FUNC(self, t):
        self.lexer.push_state('FUNC')
        print("enter func state")
        return t

    @TOKEN(ID_RE)
    def t_MAP_ID(self, t):
        return self.t_ID(t)

    @TOKEN(ID_RE)
    def t_ID(self, t):
        t.type = reserved.get(t.value, 'ID')
        return t

    @TOKEN(LBRACE_RE)
    def t_FUNC_LBRACE(self, t):
        t.type = 'FUNC_LBRACE'
        self.lexer.pop_state()
        print("exit func state")
        self.scope_level += 1
        return t

    @TOKEN(LBRACE_RE)
    def t_LBRACE(self, t):
        t.type = 'DICT_LBRACE'
        self.lexer.push_state('MAP')
        print("enter map state")
        return t

    @TOKEN(RBRACE_RE)
    def t_MAP_RBRACE(self, t):
        t.type = 'DICT_RBRACE'
        self.lexer.pop_state()
        print("exit map state")
        return t

    @TOKEN(RBRACE_RE)
    def t_RBRACE(self, t):
        t.type = 'FUNC_RBRACE'
        self.scope_level -= 1
        return t

    @TOKEN(r'\n+')
    def t_newline(self, t):
        t.lexer.lineno += len(t.value)

    def t_MAP_error(self, t):
        print(f"Illegal character in map: {t.value[0]}")
        t.lexer.skip(1)

    def t_error(self, t):
        print(f"Illegal character: {t.value[0]}")
        t.lexer.skip(1)

