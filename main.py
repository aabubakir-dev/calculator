def calculator():
    result = None

    while result is None:
        try:
            num1 = int(input("Number 1 = "))
            num2 = int(input("Number 2 = "))
        except ValueError:
            print("Введите корректное число!")
            continue

        operation = input("Введите действие (-, +, *, /): ")

        if operation not in ["-", "+", "*", "/"]:
            print("Ошибка действия, попробуйте заново")
            continue

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                print("На ноль нельзя делить! Попробуйте заново")
                continue
            result = num1 / num2

    return result


res = calculator()
print("Результат:", res)
