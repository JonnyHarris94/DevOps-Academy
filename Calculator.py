Q_file = open("calc.txt")
file_contents = Q_file.read()
contents_split = file_contents.splitlines(True)
for line in Q_file:
    fields = line.split(";")
    operation = input(fields[2])
    x = float(input(fields[3])
    y = float(input(fields[4])

    def add(x,y):
        return x + y
    def subtract(x,y):
        return x - y
    def multiply(x,y):
        return x * y
    def divide(x,y):
        return x / y

    if operation == '+':
        print(x, "+", y, "=", add(x, y))
    elif operation == '-':
        print(x, "-", y, "=", subtract(x, y))
    elif operation == '*':
        print(x, "*", y, "=", multiply(x, y))
    elif operation == '*':
        print(x, "/", y, "=", divide(x, y))
