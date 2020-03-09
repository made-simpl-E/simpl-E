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
    '{',
    '}',
    '[',
    ']',
    '.',
    ',',
    ':',
]

