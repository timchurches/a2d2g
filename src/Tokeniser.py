#! /usr/bin/env python

from ply import lex


class Lexer:
    UNIQUE_WORDS = {
        }

    tokens = [
        'WORD',
        ]

    # token regexes
    t_ignore = " \t"

    # track linenos
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # skip errors
    def t_error(self, t):
        print "illegal sequence '%s'" % t.value[0]
        t.lexer.skip(1)

    # handle words
    def t_WORD(self, t):
        r'[a-z\-_][a-z\-_0-9]*'
        t.type = self.UNIQUE_WORDS.get(t.value.lower(), 'WORD')
        return t

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)


if __name__ == '__main__':
    l = Lexer()
    l.lexer.input('this is a test but not a simple test')
    for tok in l.lexer:
        print tok
