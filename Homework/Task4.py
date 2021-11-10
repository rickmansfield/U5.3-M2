def validBracketSequence(sequence):
    pairs = dict(zip('(,[,{', '),],}'))
    stack = []
    for item in sequence:
        if item in pairs:
            stack.append(pairs[item])
        elif not (stack and item == stack.pop()):
            return False
    return not stack
