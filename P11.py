# Password Checker with 3 Attempts

correct_password = "admin123"

for i in range(3):
    password = input("Enter Password: ")

    if password == correct_password:
        print("Login Successful!")
        break
    else:
        print("Incorrect Password!")

else:
    print("Account Locked! Too many incorrect attempts.")