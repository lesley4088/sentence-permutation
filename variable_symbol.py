import Grammar


class variable_symbol(Grammar.Base):

    def __init__(self, name, grammar):
        self.name = name
        self.grammar = grammar

    def generate(self, StartVar = None):
        for word in self.grammar.generate(self.name):
            yield word

