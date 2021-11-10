def validBracketSequence(sequence):
    leftSides = ["(", "{", "["]
    rightSides = [ ")", "]", "}"]
    
    pairedDict = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    
    stack = []
    
    for char in sequence: 
        if char in leftSides: 
            stack.append(char)
        elif char in rightSides:
            if not stack or pairedDict[stack.pop()] != char:
                return False
    return len(stack) == 0