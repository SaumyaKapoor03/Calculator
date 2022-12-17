a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
out=0
op = input("Choose operation to be performed (+,-,*,/): ")
if op == '+':
    out=a+b
elif op == '-':
    out=a-b
elif op == '*':
    out=a*b
elif op == '/':
    while b==0:
        print("Error! Please enter a number other than 0")
        b = int(input("Enter second number: "))
    out=a/b
else:
    out="Enter a valid operation!"
print(a, op, b, "=",out)