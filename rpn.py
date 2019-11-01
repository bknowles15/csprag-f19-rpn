#!/usr/bin/env python3

import operator

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mult(a, b):
    return a * b

def exp(a, b):
    return a ** b


OPS = {
    '+': operator.add, 
    '-': operator.sub,
    '/': operator.truediv, 
    '*': operator.mul, 
    '^': operator.pow
}

def calculate(arg):
    items = arg.split()
    stack = []
    for item in items:
        try:
            value = int(item)
            stack.append(value)
        except ValueError:
            function = OPS[item]
            if len(stack) < 2:
                raise TypeError('Malformed input')
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(function(num2, num1))
    if len(stack) != 1:
        raise TypeError('Malformed input')
    return stack.pop()


def main():
    while True:
        result = calculate(input("rpn calc>"))
        print(result)

if __name__ == '__main__':
    main()
