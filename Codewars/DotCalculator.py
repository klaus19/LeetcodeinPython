class Solution(object):

    def getCalculator(self,s):

        left_s,right_s,op_str = s.split()

        left_operand = int(left_s.count('.'))
        right_operand = int(right_s.count('.'))
        # Perform the appropriate operation based on the operator
        if op_str == "+":
            result = left_operand + right_operand
        elif op_str == "-":
            result = left_operand - right_operand
        elif op_str == "*":
            result = left_operand * right_operand
        elif op_str == "/":
            result = left_operand / right_operand
        else:
            raise ValueError("Invalid operator: {}".format(op_str))

        # Convert the result to a string and replace each digit with a dot
        result_str = "." * result

        return result_str
