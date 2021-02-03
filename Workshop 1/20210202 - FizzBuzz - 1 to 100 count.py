for number in range (1,201):
    string = ""

    if number % 3 == 0:
        string += "Fizz"
    if number % 13 == 0:
        string += "Fezz"
    if number % 5 == 0:
        string += "Buzz"
    if number % 7 == 0:
        string += "Bang"
    elif number % 11 == 0 and number % 13 ==0:
        string = "FezzBong"
    elif number % 11 == 0:
        string = "Bong"


    
    if string == "":
        print(number)
    else:
        print(string)
