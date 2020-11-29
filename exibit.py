#Exercise 3
integer = int(input("Please enter an integer to get a hash square: "))

def square(int_input):
    count = 0
    row = "#"*int_input
    while count < int_input:
        print(row)
        count += 1

square(integer)