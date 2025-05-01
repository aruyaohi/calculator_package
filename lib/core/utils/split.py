from typing import Union, List

class Split:
    def __init__(self,expression:str):
        self.expression = expression
        
    def get_expression(self):
        return self.expression
    
    #custom split method:
    def split(self):
        result_list = []
        current_token = ''
        for item in self.expression:
            if item != ',':
                current_token += item
            else:
                result_list.append(current_token)
                #A rest to the current token for next loop or interval
                current_token = ''

        result_list.append(current_token)
       
        return result_list

