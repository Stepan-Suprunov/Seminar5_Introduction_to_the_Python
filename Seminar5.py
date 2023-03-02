# Требуется найти N-e число фибоначчи.


n = int(input('Введите номер искомого числа Фибоначчи: '))
fib = [0, 1, 1]
if n < 1:
    print('Введите положительное число')
elif n == 1:
    print(0)
elif 1 < n < 4:
    print(1)
else:
    for i in range(2, n-1):
        fib.append(fib[i-1] + fib[i])
    print(fib[-1])


# С помощью рекурсии:

def fibonacci(num):
    if num <= 1:
        fib = 0
    elif 1 < num < 4:
        fib = 1
    else:
        fib = fibonacci(num-1) + fibonacci(num-2)
    print(fib)
    return fib

n = int(input('Введите номер искомого числа Фибоначчи: '))
print(fibonacci(n))


# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

Vasily_marks = [int(input('Введите оценку: ')) for _ in range(int(input('Введите колл-во оценок: ')))]
print(Vasily_marks)

min_mark = 5
max_mark = 1
for i in Vasily_marks:
    if i < min_mark:
        min_mark = i
    if i > max_mark:
        max_mark = i

for j in range(len(Vasily_marks)):
    if Vasily_marks[j] == max_mark:
        Vasily_marks[j] = min_mark

print(Vasily_marks)


# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.

def simple(n):
    if n == 2:
        return "Число простое"
    for i in range(2, n):
        if n % i == 0:
            return 'Число составное'
        return "Число простое"

num = int(input('Введите число: '))
print(simple(num))
