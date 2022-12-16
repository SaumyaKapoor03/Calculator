a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation to be performed: ")
if op == 'addition':
    out=a+b
elif op == 'subtraction':
    out=a-b
elif op == 'multiplication':
    out=a*b
elif op == 'division':
    out=a/b
else:
    out="Enter valid operation!"
print(out)