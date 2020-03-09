reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'in': 'IN',
    'func': 'FUNC'
}

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
    'COMMENT',
) + tuple(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

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

