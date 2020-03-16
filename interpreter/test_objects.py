class LexerTestResults(object):
    def __init__(self):
        self.test_tokens = []

    def add_tok(self, tok, col):
        self.test_tokens.append(TestToken(tok, col))

    def print(self):
        for tok in self.test_tokens:
            print(tok)


class TestObject(object):
    pass

class TestToken(TestObject):
    def __init__(self, tok, col):
        self.tok = tok
        self.col = col

    def __repr__(self):
        return repr(self.tok) + f", Column: {repr(self.col)}"

    def __str__(self):
        return str(repr(self))

