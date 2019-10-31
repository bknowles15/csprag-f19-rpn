#!/usr/bin/env python3

OPS = {'+', '-', '/', '*', '^'}

def do_operation(op, num1, num2):
    if op == '+':
        return num1 + num2
    if op == '-':
        return num2 - num1
    if op == '*':
        return num1 * num2
    if op == '^':
        return num2 ** num1
    if op == '/':
        return num2 / num1
    raise TypeError('Unrecognized operator')


def calculate(arg):
    items = arg.split()
    stack = []
    for item in items:
        if item in OPS:
            if len(stack) < 2:
                raise TypeError('Malformed input')
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(do_operation(item, num1, num2))
        else:
            stack.append(int(item))
    if len(stack) != 1:
        raise TypeError('Malformed input')
    return stack.pop()


def main():
    while True:
        calculate(input("rpn calc"))

if __name__ == '__main__':
    main()
