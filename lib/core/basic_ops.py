# import math
from typing import List

class BasicOperations:
    def __init__(self,operand_one: float,operand_two:float):
        self.operand_one = operand_one
        self.operand_two = operand_two

    def add(self) -> float:
        """Adds two numbers."""
        return self.operand_one + self.operand_two

    def subtract(self) -> float:
        """Subtracts the second number from the first."""
        return self.operand_one - self.operand_two

    def multiply(self) -> float:
        """Multiplies two numbers."""
        return self.operand_two * self.operand_two

    def divide(self) -> float :
        """Divides the first number by the second. Returns an error message if the divisor is zero."""
        if self.operand_two == 0:
            return "Error: Division by zero"
        return self.operand_one / self.operand_two