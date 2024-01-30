class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Dictionary mapping operators to corresponding lambda functions
        operations = {"+": lambda a, b: a + b,
                      "-": lambda a, b: a - b,
                      "/": lambda a, b: int(a / b),
                      "*": lambda a, b: a * b
                     }
        
        # Stack to store operands
        stack = []
        
        # Iterate through each token in the input list
        for val in tokens:
            # If the token is an operator, perform the corresponding operation using the lambda function
            if val in operations:
                y = stack.pop()
                x = stack.pop()
                # Push the result of the operation back onto the stack
                stack.append(operations[val](x, y))
            else:
                # If the token is an operand, convert it to an integer and push onto the stack
                stack.append(int(val))
        
        # The final result is the only element left in the stack
        return stack[0]