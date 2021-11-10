"""
This is the faster version. 
It uses dictionaires hence it can search 
faster by key rather than linear search. 

also note the only difference between Stack and Queue would 
be added a zero inside pop(). The only difference is which end
the pop() function removes the item from. 
"""
def validBracketSequence(sequence):
    leftSides = set(["(", "{", "["])
    rightSides = set([ ")", "]", "}"])
    
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