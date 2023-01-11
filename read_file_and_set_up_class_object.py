import Grammar

def read_and_creat_object(path):
    grammar = Grammar.grammar()
    with path.open() as file:
        content = file.readlines()
        content = [line[0:-1] if line[-1] == "\n" else line for line in content]
        i = 0
        while i < len(content):
            if content[i] == '{':
                rule_start = True
                variableName = content[i + 1]
                rule = Grammar.rule(variableName)
                i += 2
                j = i
                while rule_start:
                    if content[j] == '}':
                        rule_start = False
                        j += 1
                    else:
                        option = Grammar.option()
                        currentLine = content[j].split(' ')
                        if len(currentLine) == 1:
                            currentLine.append('')

                        for char in currentLine[1:]:
                            if char.startswith('[') and char.endswith(']'):
                                symbol = Grammar.variable_symbol(char[1:-1], grammar)
                            else:
                                symbol = Grammar.terminal_symbol(char)
                            option.addSymbol(symbol)
                        for x in range(int(currentLine[0])):
                            rule.addOption(option)

                        j += 1
                    grammar.addRule(variableName, rule)

                i = j
            else:
                i += 1

    return grammar
