def sum(a, b):
    result = a + b
    return result
def minus(a, b):
    result = a - b
    return result
def multiplication(a, b):
    result = a * b
    return result
def division(a, b):
    result = a / b
    return result
    
a = input("첫번째 숫자 입력: ")
b = input("두번째 숫자 입력: ")
operation = input("연산 선택(+-*/): ")

if operation == '+':
    c = sum(a, b)
elif operation == '-':
    c = minus(a, b)
elif operation == '*':
    c = multiplication(a, b)
elif operation == '/':
    c = division(a, b)    
print(c)