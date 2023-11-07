counter = 0
sum = 0
positive_integer_as_string = input("Please enter a positive integer:")

try:
    positive_integer_as_int = int(positive_integer_as_string)
    while counter <= positive_integer_as_int:
        sum = sum + counter
        counter = counter + 1
    print(f"Sum of numbers is {sum}")
except:
    print("Not a valid integer")
