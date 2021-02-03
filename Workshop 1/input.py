def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

Operation = input ('Define Operation')
x = float(input ('Define x: '))
y = float(input ('Define y: '))

if Operation == '+':
    print (x,"+",y, "=", add(x, y))
elif Operation == '-':
    print (x,"-",y, "=", subtract(x, y))
elif Operation == '*':
    print (x,"*",y, "=", multiply(x, y))
elif Operation == '*':
    print (x,"/",y, "=", divide(x, y))
