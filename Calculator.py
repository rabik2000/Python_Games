# This is a calculator that does basic operations
def error_handle():
    if second == 0:
        print("The answer is infinity \n")
    else:
         print("Result: ", first/second)



print("This is a Calculator that does basic mathematical operations \n")
print("The operations that we do are Addition = +, Subtraction = - , Multiplication = * and Division = / \n")
print("Now let us take inputs for our operation: \n")

first = float(input("Enter your first value: "))
second = float(input("Enter your second value: "))

print("Select the operation to be done: +  -   *  /   \n")
operation = str(input("Please only select the options as shown above:  "))

if operation == "+":
    print("Result: ", first+second)
elif operation == "-":
    print("Result:  ", first-second)
elif operation == "*":
    print("Result:  ", first*second)
elif operation == "/":
    error_handle()
   