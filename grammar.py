import Grammar

class grammar(Grammar.Base):

    def __init__(self):
        self.Rules = {}

    def addRule(self, variable, rule):
        self.Rules[variable] = rule

    def getRules(self):
        result = {}
        for rule in self.Rules.keys():
            result[rule] = self.Rules[rule].getRule()
        return result

    def generate(self, StartVar = None):
        for word in self.Rules[StartVar].generate():
            yield word