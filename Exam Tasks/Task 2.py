
"""
Task 2

"""

# The list acts as table, where the index 0 = decimal 1, index 1 = decimal 2 and so forth.
binary_table = ["0001","0010","0011","0100","0101","0110","0111","1000","1001","1010"]

print() # This print is only here to provide better spacing when viewing the terminal output

"""
This function takes the decimal number as an input and prints the binary value of it from the binary_table, and then prints it in a formatted table using formatting

"""
def decimal_to_binary(number):
    if number < 1 or number > 10:
        print("Invalid number")
        return
    print("Decimal".ljust(10) + "|" + " Binary")
    print(str(number).ljust(10) + "| " + binary_table[number - 1])

user_input = int(input("Enter a decimal number (1-10): "))
decimal_to_binary(user_input)

print() # This print is only here to provide better spacing when viewing the terminal output