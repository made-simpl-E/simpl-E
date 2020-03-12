reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'in': 'IN',
    'func': 'FUNC',
}

tokens = (
    'INT',
    'FLOAT',
    'EQ',
    'GEQ',
    'LEQ',
    'IDENTIFIER',
    'PLUS_ASSIGNMENT',
    'MINUS_ASSIGNMENT',
    'TIMES_ASSIGNMENT',
    'DIVIDE_ASSIGNMENT',
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

