def generateStatement(grammar, startVar, count):
    for i in range(count):
        sentence = ''
        for word in grammar.generate(startVar):
            sentence += word + " "
        yield sentence[0:len(sentence) - 1]