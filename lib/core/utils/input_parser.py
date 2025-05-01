from typing import List
from utils.split import Split
precendence = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '^' : 3
}

associativity = {
    '+' : 'L',
    '-' : 'L',
    '*' : 'L',
    '/' : 'L',
    '^' : 'R'
}

class input_parser:
    def __init__(self,expression: str):
        self.expression = expression

    def parse(self):
        tokens = Split(self.expression)
        split_token = tokens.split()
        stack = []
        output = []

        for token in split_token:
            if token.isnumeric():
                output.append(token)
            elif token in precendence:
                while(stack and stack[-1] in precendence and ((associativity[token] == "L" and precendence[token] <= precendence[stack[-1]]) or (associativity[token] == 'R' and precendence[token] < precendence[stack[-1]]))):
                  output.append(stack.pop())
                stack.append(token)
        
        while stack:
                output.append(stack.pop())
        return output

