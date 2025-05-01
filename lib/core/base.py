import math
from abc import ABC, abstractmethod
from typing import List
from utils.input_parser import input_parser


local_operators = ['+','-','*','/']

class Calculator:
    def __init__(self, expression: str):
        self.expression = expression

    def calculate(self):
        numbers = []
        operators = []
        expression = input_parser(self.expression)
        result = expression.parse()
        for item in result:
            if item.isnumeric():
                numbers.append(item)
            elif item in local_operators:
                operators.append(item)
      
        return numbers,operators
        

expression_one = Calculator('3,+,5,*,8')
print(expression_one.calculate())

    