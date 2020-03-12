import ply.yacc as yacc

from tokens import tokens


class SimpleParser:

    tokens = tokens

    precedence = (
        ('right', '=', 'PLUS_ASSIGNMENT', 'MINUS_ASSIGNMENT', \
                'TIMES_ASSIGNMENT', 'DIVIDE_ASSIGNMENT'),
        ('left', 'EQ'),
        ('left', 'LEQ', 'GEQ'),
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
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
            print(result)

    def p_expression(self, p):
        '''expression : '(' expression ')'
                      | number
                      | assignment
                      | unary_op
                      | binary_op
                      | IDENTIFIER'''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_assignment(self, p):
        '''assignment : IDENTIFIER '=' expression
                      | IDENTIFIER PLUS_ASSIGNMENT expression
                      | IDENTIFIER MINUS_ASSIGNMENT expression
                      | IDENTIFIER TIMES_ASSIGNMENT expression
                      | IDENTIFIER DIVIDE_ASSIGNMENT expression'''
        p[0] = p[3]

    def p_binary_op(self, p):
        '''binary_op : expression '+' expression
                     | expression '-' expression
                     | expression '*' expression
                     | expression '/' expression'''
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]

    def p_unary_op(self, p):
        '''unary_op : '-' expression %prec UMINUS'''
        p[0] = -p[2]

    def p_number(self, p):
        '''number : INT
                  | FLOAT'''
        p[0] = p[1]

    def p_error(self, p):
        print("Syntax error in input!")

