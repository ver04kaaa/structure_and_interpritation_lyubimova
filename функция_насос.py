def pump_function(a, x, y):
    def function1():
        return a + b_function()

    def b_function():
        return x * 7 + c_function()

    def c_function():
        return y * 3

    def result_function():
        return function1()

    return result_function()

# Пример использования функции насоса
a = 5
x = 2
y = 3
print(pump_function(a, x, y))  # Выводит: 35
