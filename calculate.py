
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Please Select Operation")
print("Press 1. for Addition")
print("Press 2. for Subtraction")
print("Press 3. for Multiplication")
print("Press 4. for Division")


while True:
    choice = input("1/2/3/4:"  )
    if choice not in ('1', '2', '3', '4'):
        print("You have enter Invalided Choice, Please Enter the correct operation")
        continue

    try:
        num1 = float(input("Enter First Number:  "))
        num2 = float(input("Enter Second Number:  "))
    except ValueError:
        print("You Must Enter Number Only")
        continue

    if choice == '1':
        print(f'{num1} + {num2} = {add(num1, num2)}')
    elif choice == '2':
        print(f'{num1} - {num2} = {subtract(num1, num2)}')
    elif choice == '3':
        print(f'{num1} * {num2} = {multiply(num1, num2)}')
    elif choice == '2':
        print(f'{num1} / {num2} = {divide(num1, num2)}')
    else:
        print("Incorrect Choice")
