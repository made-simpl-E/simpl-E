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
    'LBRACE',
    'RBRACE',
    'LSQBRACE',
    'RSQBRACE',
    'PERIOD',
    'COMMA',
    'COLON',
    'ID',
    'COMMENT',
) + tuple(reserved.values())

