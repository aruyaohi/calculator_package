import math
from abc import ABC, abstractmethod
from typing import List
from utils.input_parser import input_parser


operators = {

}

class Calculator:
    def __init__(self, expression: str):
        self.expression = expression

    def calculate(self):
        numbers = []
        operators = []
        expression = input_parser(self.expression)
        result = expression.parse()
        print(result)
        # numbers = (result['output'])
        # operators = (result['operators'])

        print(numbers,operators)
        

expression_one = Calculator('3,+,5,*,8')
expression_one.calculate()
    