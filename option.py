import Grammar

class option(Grammar.Base):

    def __init__(self):
        self.symbols = []

    def addSymbol(self, symbol):
        self.symbols.append(symbol)


    def getOptions(self):
        result = []
        for symbol in self.symbols:
            if isinstance(symbol, Grammar.variable_symbol):
                result.append('[' + symbol.name + ']')
            elif isinstance(symbol, Grammar.terminal_symbol):
                result.append(symbol.terminal)
        return result

    def generate(self, StartVar = None):
        for symbol in self.symbols:
            for word in symbol.generate():
                yield word
