import ply.lex as lex
from ply.lex import TOKEN

from tokens import literals, tokens, reserved
from re_strings import *
from test_objects import LexerTestResults


class SimpleLexer(object):
    literals = literals

    tokens = tokens

    reserved = reserved

    def __init__(self, test_mode=False, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.current_indentation = ''
        self.test_mode = test_mode

    def input(self, data):
        self.lexer.input(data)

    def test(self, data):
        self.input(data)
        if self.test_mode:
            results = LexerTestResults()
        for tok in self.lexer:
            if self.test_mode:
                results.add_tok(tok, self.find_column(data, tok))
            else:
                print(tok)
        if self.test_mode:
            return results

    def token(self):
        return self.lexer.token()

    @staticmethod
    def find_column(data, token):
        line_start = data.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

    t_ignore = ' \t'
    t_EQ = r'=='
    t_GEQ = r'>='
    t_LEQ = r'<='
    t_PLUS_ASSIGNMENT = r'\+='
    t_MINUS_ASSIGNMENT = r'-='
    t_TIMES_ASSIGNMENT = r'\*='
    t_DIVIDE_ASSIGNMENT = r'\/='
    t_ignore_COMMENT = r'\#.*'

    @TOKEN(LBRACE_RE)
    def t_lbrace(self, t):
        t.type = '{'
        return t

    @TOKEN(RBRACE_RE)
    def t_rbrace(self, t):
        t.type = '}'
        return t

    @TOKEN(LPAREN_RE)
    def t_lparen(self, t):
        t.type = '('
        return t

    @TOKEN(RPAREN_RE)
    def t_rparen(self, t):
        t.type = ')'
        return t

    @TOKEN(FLOAT_RE)
    def t_FLOAT(self, t):
        t.value = float(t.value)
        return t

    @TOKEN(INT_RE)
    def t_INT(self, t):
        t.value = int(t.value)
        return t

    @TOKEN(ID_RE)
    def t_IDENTIFIER(self, t):
        t.type = reserved.get(t.value, 'IDENTIFIER')
        return t

    @TOKEN(r'\n+')
    def t_newline(self, t):
        t.lexer.lineno += len(t.value)
        t.type = 'NEWLINE'
        return t

    def t_error(self, t):
        print(f"Illegal character: {t.value[0]}")
        t.lexer.skip(1)

