import operator


class Stack(object):
    """
    Last in first out data structure / first in last out.

    Ideal for:
    - operations that have repetitive components/transformations
       (e.g. reverse polish notation) where recurison can be useful.
    - undoing actions (e.g. popping code change off a stack!)
    """

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def is_empty(self):
        return self.size() <= 0

    def size(self):
        return len(self.stack)


def reverse_polish_notation(expression):
    operator_to_func_map = {
        '+': operator.add,
        '-': operator.sub,
        '/': operator.truediv,
        '*': operator.mul,
        '**': operator.pow
    }

    valid_arg = (lambda x: x.isdigit() or x in operator_to_func_map.keys())
    args = expression.split(' ')
    stack = Stack()
    for arg in args:  # Big O(n)
        if not valid_arg(arg):
            return None
        if arg in operator_to_func_map.keys():
            operand_two = float(stack.pop())
            operand_one = float(stack.pop())
            stack.push(operator_to_func_map.get(arg)(operand_one, operand_two))
        else:
            stack.push(arg)

    return stack.pop()


if __name__ == '__main__':

    reverse_polish_notation('3 5 +') == 8
    reverse_polish_notation('3 5 + 10 *') == 80
    reverse_polish_notation('10 3 5 + *') == 80
