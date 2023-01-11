import Grammar
import random

class rule(Grammar.Base):

    def __init__(self, name):
        self.variable = name
        self.options = []

    def addOption(self, option):
        self.options.append(option)


    def getRule(self):
        result = []
        for option in self.options:
            result.append(option.getOptions())
        return result


    def generate(self, StartVar = None):
        index = random.randint(0, len(self.options) - 1)
        for word in self.options[index].generate():
            yield word