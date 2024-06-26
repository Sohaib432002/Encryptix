

 #Task no 2
#Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.


def perform_operation(number_1, number_2, operation):
    if operation == 1:
        result = number_1 + number_2
        operation_name = "Addition"
        symbol = "+"
    elif operation == 2:
        result = number_1 - number_2
        operation_name = "Subtraction"
        symbol = "-"
    elif operation == 3:
        result = number_1 * number_2
        operation_name = "Multiplication"
        symbol = "x"
    elif operation == 4:
        if number_2 == 0:
            return "Error: Division by zero is not allowed."
        result = number_1 / number_2
        operation_name = "Division"
        symbol = "/"
    else:
        return "Invalid operation! Please enter a number between 1 and 4."

    string=operation_name,"of the numbers " ,number_1, "&", number_2 ,"is" ,result
    return string


def get_user_input():
    number_1 = float(input("Enter the first number: "))
    number_2 = float(input("Enter the second number: "))

    print("Which operation would you like to perform?")
    print(" Addition (+)         Press -1 ")
    print(" Subtraction (-)    Press -2    ")
    print(" Multiplication (x) Press -3")
    print(" Division (/)       Press -4 ")

    operation = int(input("Please enter the number corresponding to the operation (1/2/3/4): "))
    while operation >= 5 or operation <= 0:
        print('Please Input Number between 1 to 4')
        operation = int(input("Please enter the number corresponding to the operation (1/2/3/4): "))

    return number_1, number_2, operation


def main():
    number_1, number_2, operation = get_user_input()
    print(perform_operation(number_1, number_2, operation))

if __name__ == "__main__":
    main()
