class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if len(tokens) == 1:
        #     return int(tokens[0])

        stack = []
        operands = ["+","-","*","/"]

        for token in tokens:
            if token == "+":
               op1 = stack.pop()
               op2 = stack.pop()
               print(op1,op2,"+",op1 + op2)
               stack.append(op1 + op2)
               print(f"Summed stack: {stack}")

            elif token == "-":
               op1 = stack.pop()
               op2 = stack.pop()
               print(op1,op2,"-",op2 - op1)
               stack.append(op2 - op1)
               print(f"Subtracted stack: {stack}")

            elif token == "*":
               op1 = stack.pop()
               op2 = stack.pop()
               print(op1,op2,"*",op1 * op2)
               stack.append(op1 * op2)
               print(f"Multiplied stack: {stack}") 

            elif token == "/":
               op1 = stack.pop()
               op2 = stack.pop()
               print(op1,op2,"/",op2//op1)
               stack.append(int(op2/op1))
               print(f"Divided stack: {stack}")

            else:
                stack.append(int(token))
                print(stack)

        return stack[0]
        