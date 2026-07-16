try:
    a = int(input("Enter a: "))

    if a < 1:
        raise ValueError

    print(a)

except ValueError:
    print("b")