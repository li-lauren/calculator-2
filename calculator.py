"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    exp = input("Enter an expression: ")
    exp_tokens = exp.split(' ')
    if exp_tokens[0] == "q" or exp_tokens[0] == "Q":
        break
    else:
        for index in range(1, len(exp_tokens)):
            exp_tokens[index] = int(exp_tokens[index])
            
        if exp_tokens[0] == "+":
            answer = (add(exp_tokens[1], exp_tokens[2]))

        elif exp_tokens[0] == "-":
            answer = subtract(exp_tokens[1], exp_tokens[2])

        elif exp_tokens[0] == "*":
            answer = multiply(exp_tokens[1], exp_tokens[2])
        
        elif exp_tokens[0] == "/":
            answer = divide(exp_tokens[1], exp_tokens[2])

        elif exp_tokens[0] == "square":
            answer = square(exp_tokens[1])

        elif exp_tokens[0] == "cube":
            answer = cube(exp_tokens[1])

        elif exp_tokens[0] == "pow":
            answer = power(exp_tokens[1], exp_tokens[2])

        elif exp_tokens[0] == "mod":
            answer = mod(exp_tokens[1], exp_tokens[2])

        else:
            answer = 'Invalid expression.'

    print(answer)


