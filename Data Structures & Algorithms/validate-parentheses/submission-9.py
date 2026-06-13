class Solution:
    def isValid(self, s: str) -> bool:
        validPairs = {"]" : "[", "}" : "{", ")" : "("}
        stack = []

        for p in s:
            #If the current char is a closing parentheses
            if p in validPairs:
                #checks whether the top of the stack is the matching opening parenthesis 
                if stack and stack[-1] == validPairs[p]:
                    stack.pop()
                else:
                    #it is not a valid pair so return False
                    return False
            #if this is a opening parenthese add it into the stack
            else:
                stack.append(p)
        #if the stack is empty it means we have found all valid pairs so we return True
        #otherwise return False
        return True if not stack else False
