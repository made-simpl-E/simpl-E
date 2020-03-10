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
        self.find_func_id = False
        self.find_func_args = False
        self.current_indentation = ''

    def input(self, data):
        self.lexer.input(data)

    def test(self, data):
        self.input(data)
        for tok in self.lexer:
            print(self.current_indentation * self.scope_level + str(tok))

    def token(self):
        return self.lexer.token()

    t_ignore = r' '
    t_EQ = '=='
    t_GEQ = '>='
    t_LEQ = '<='
    t_MAP_ignore = r' '
    t_ignore_COMMENT = r'\#.*'

    def _push_scope(self):
        self.scope_level += 1
        self.current_indentation += '    '

    def _pop_scope(self):
        self.scope_level -= 1
        self.current_indentation = self.current_indentation[:-4]

    @TOKEN(INT_RE)
    def t_MAP_INT(self, t):
        return self.t_INT(t)

    @TOKEN(INT_RE)
    def t_INT(self, t):
        t.value = int(t.value)
        return t

    @TOKEN(FLOAT_RE)
    def t_MAP_FLOAT(self, t):
        return self.t_FLOAT(t)

    @TOKEN(FLOAT_RE)
    def t_FLOAT(self, t):
        t.value = float(t.value)
        return t

    @TOKEN('func')
    def t_FUNC(self, t):
        self.lexer.push_state('FUNC')
        self.find_func_id = True
        return t

    @TOKEN(ID_RE)
    def t_MAP_IDENTIFIER(self, t):
        return self.t_IDENTIFIER(t)

    @TOKEN(ID_RE)
    def t_IDENTIFIER(self, t):
        t.type = reserved.get(t.value, 'IDENTIFIER')
        if t.type == 'IDENTIFIER':
            if self.find_func_id:
                t.type = 'FUNC_IDENTIFIER'
                self.find_func_id = False
                self.find_func_args = True
            elif self.find_func_args:
                t.type = 'FUNC_ARG_IDENTIFIER'

        return t

    @TOKEN(LBRACE_RE)
    def t_FUNC_lbrace(self, t):
        t.type = '{'
        self._push_scope()
        self.find_func_args = False
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

    @TOKEN(LPAREN_RE)
    def t_lparen(self, t):
        if self.find_func_args:
            t.type = 'FUNC_LPAREN'
        else:
            t.type = '('
        return t

    @TOKEN(RPAREN_RE)
    def t_rparen(self, t):
        if self.find_func_args:
            t.type = 'FUNC_RPAREN'
        else:
            t.type = ')'
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

