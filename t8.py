class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y
calculator = Calculator()
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    result = calculator.add(num1, num2)
elif choice == '2':
    result = calculator.subtract(num1, num2)
elif choice == '3':
    result = calculator.multiply(num1, num2)
elif choice == '4':
    result = calculator.divide(num1, num2)
else:
    result = "Invalid input"
print(f'{result} is the result')
