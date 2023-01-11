import Grammar

class terminal_symbol(Grammar.Base):

    def __init__(self, terminal):
        self.terminal = terminal

    def generate(self, StartVar = None):
        yield self.terminal

