import ply.yacc as yacc

from tokens import tokens


class SimpleParser:

    tokens = tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
    )

    def __init__(self, lexer):
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer

    def parse(self, data, lexer=None):
        if not lexer:
            lexer = self.lexer
        return self.parser.parse(data, lexer=lexer)

    def test(self):
        while True:
            try:
                data = input('[ simpl-E ] >> ')
            except EOFError:
                break
            if not data: continue
            if data.lower() == 'exit':
                break
            result = self.parse(data)
            print(data)

    def p_expression(self, p):
        '''expression : expression '+' expression
                      | expression '-' expression
                      | expression '*' expression
                      | expression '/' expression
                      | '(' expression ')'
                      | NUMBER'''
        if len(p) == 2:
            p[0] = p[1]
            return
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        else:
            p[0] = p[2]

    def p_error(self, p):
        print("Syntax error in input!")

