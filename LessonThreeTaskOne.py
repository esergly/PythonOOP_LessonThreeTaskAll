try:
    price = float(input())
    if price < 0:
        raise ArithmeticError
except ArithmeticError:
    print("The price value should be equal or bigger then zero")
except ValueError:
    print("The price value should be entered as digits only")
else:
    print(price)
