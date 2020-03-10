reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'in': 'IN',
}

tokens = (
    'NUMBER',
    'FUNC',
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

