print("########CALCULATOR########")
print(" 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Remainder")
num = int(input("Enter Your Choice: "))

if (num == 1):
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2st Number: "))
    print(num1 + num2)

elif (num == 2):
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2st Number: "))
    print(num1 - num2)

elif (num == 3):
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2st Number: "))
    print(num1 * num)

elif (num == 4):
    num1 = float(input("Enter 1st Number: "))
    num2 = float(input("Enter 2st Number: "))
    print(num1 / num2)

elif (num == 5):
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2st Number: "))
    print(num1 % num2)