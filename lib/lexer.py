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
        self.current_indentation = ''

    def input(self, data):
        self.lexer.input(data)

    def test(self, data):
        self.input(data)
        for tok in self.lexer:
            print(self.current_indentation * self.scope_level + str(tok))

    t_ignore = r' '
    t_MAP_ignore = r' '
    t_ignore_COMMENT = r'\#.*'

    def _push_scope(self):
        self.scope_level += 1
        self.current_indentation += '    '

    def _pop_scope(self):
        self.scope_level -= 1
        self.current_indentation = self.current_indentation[:-4]

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
        return t

    @TOKEN(ID_RE)
    def t_MAP_ID(self, t):
        return self.t_ID(t)

    @TOKEN(ID_RE)
    def t_ID(self, t):
        t.type = reserved.get(t.value, 'ID')
        return t

    @TOKEN(LBRACE_RE)
    def t_FUNC_lbrace(self, t):
        t.type = '{'
        self._push_scope()
        return t

    @TOKEN(LBRACE_RE)
    def t_lbrace(self, t):
        t.type = '{'
        return t

    @TOKEN(RBRACE_RE)
    def t_FUNC_rbrace(self, t):
        t.type = '}'
        self._pop_scope()
        self.lexer.pop_state()
        return t

    @TOKEN(RBRACE_RE)
    def t_rbrace(self, t):
        t.type = '}'
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

