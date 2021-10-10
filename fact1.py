def factorial(num):
    operation = []
    for i in range(1, num+1):
        operation.append(str(i))
        operation.append("*")
    operation = "".join(operation)
    operation = operation[:-1]
    return eval(operation)

print(factorial(int(input())))
