num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

operation = input("Введите операцию (+, -, *, /): ")

if operation == '+':
    print(f"Результат {num1 + num2}")

elif operation == '-':
    print(f"Result = {num1 - num2}")

elif operation == "*":
    print(f"Result = {num1 * num2}")

else:
    print(f"Result = {num1 / num2}")