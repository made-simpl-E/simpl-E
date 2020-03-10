reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'in': 'IN',
}

tokens = (
    'INT',
    'FLOAT',
    'FUNC',
    'FUNC_IDENTIFIER',
    'FUNC_ARG_IDENTIFIER',
    'FUNC_LPAREN',
    'FUNC_RPAREN',
    'EQ',
    'GEQ',
    'LEQ',
    'IDENTIFIER',
    'COMMENT',
) + tuple(reserved.values())

literals = [
    '+',
    '-',
    '*',
    '/',
    '(',
    ')',
    '{',
    '}',
    '[',
    ']',
    '.',
    ',',
    ':',
    '=',
    '<',
    '>',
]

states = (
    ('MAP', 'exclusive'),
    ('FUNC', 'inclusive'),
)

