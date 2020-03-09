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
    'FUNC_LBRACE',
    'FUNC_RBRACE',
    'DICT_LBRACE',
    'DICT_RBRACE',
    'ID',
    'COMMENT',
) + tuple(reserved.values())

literals = [
    '+',
    '-',
    '*',
    '/',
    '(',
    ')',
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

