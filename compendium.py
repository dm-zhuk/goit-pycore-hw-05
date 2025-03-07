#!/usr/bin/python
# -*- coding: utf-8 -*-


import collections
from collections import Counter, defaultdict, namedtuple, deque
from decimal import Decimal as d, getcontext

"""
print(d("0.1") + d("0.2") == d("0.3"))
print(d("0.1") + d("0.2"))


getcontext().prec = 6
print(d("1") / d("7"))

getcontext().prec = 8
print(d("1") / d("7"))


def create_stack():
    return []


def is_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("empty stack")


def peek(stack):
    if not is_empty(stack):
        return stack(-1)
    else:
        print("empty stack")


stack = create_stack()
push(stack, "a")
push(stack, "b")
push(stack, "c")
push(stack, "Ann")
print(stack)
pop(stack)

print(stack)


Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

cat = Cat("Simon", 4, "Krabat")

print(f"This is {cat.nickname}, a {cat.age}-year-old cat. His owner is {cat.owner}.")
print(f"This is a cat {cat[0]}, {cat[1]} age, his owner {cat[2]}")

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1

print(mark_counts)
student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_count = collections.Counter(student_marks)
print(mark_count.most_common())
print(mark_count.most_common(1))
print(mark_count.most_common(2))

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = Counter(words)

# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")

# Створення defaultdict з list як фабрикою за замовчуванням
d = defaultdict(list)

# Додавання елементів до списку для кожного ключа
d["a"].append(1)
d["a"].append(2)
d["b"].append(4)

print(d)

words = ["apple", "zoo", "lion", "lama", "bear", "bet", "wolf", "appendix"]
grouped_words = defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(dict(grouped_words))
# Створення пустої двосторонньої черги
d = deque()

# Додаємо елементи в чергу
d.append("middle")  # Додаємо 'middle' в кінець черги
d.append("last")  # Додаємо 'last' в кінець черги
d.appendleft("first")  # Додаємо 'first' на початок черги

# Виведення поточного стану черги
print("Черга після додавання елементів:", list(d))

# Видалення та виведення останнього елемента (з правого кінця)
print("Видалений останній елемент:", d.pop())

# Видалення та виведення першого елемента (з лівого кінця)
print("Видалений перший елемент:", d.popleft())

# Виведення поточного стану черги після видалення елементів
print("Черга після видалення елементів:", list(d))

# Список завдань, де кожне завдання - це словник
tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"},
]

# Ініціалізація черги завдань
task_queue = deque()

# Розподіл завдань у чергу відповідно до їх пріоритету
for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)  # Додавання на високий пріоритет
        print(f"Додано швидке завдання: {task['name']}")
    else:
        task_queue.append(task)  # Додавання на низький пріоритет
        print(f"Додано повільне завдання: {task['name']}")

# Виконання завдань
while task_queue:
    task = task_queue.popleft()
    print(f"Виконується завдання: {task['name']}")


def my_function():
    print("Hello, world!")


f = my_function
f()

from typing import Callable


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)


# Використання
result_add = apply_operation(5, 3, add)
result_multiply = apply_operation(5, 3, multiply)

print(result_add, "|", result_multiply)


def make_counter():
    count = 0  # Змінна з зовнішньої функції

    def count_up():  # Внутрішня функція
        nonlocal count  # Доступ до змінної count
        count += 1
        return count

    return count_up  # Повертаємо внутрішню функцію


# Використання
counter = make_counter()  # Створюємо лічильник

print(counter())  # Виведе: 1
print(counter())  # Виведе: 2
print(counter())  # Виведе: 3


def add(a):
    def add_b(b):
        return a + b

    return add_b


# Використання:
add_5 = add(5)
result = add_5(10)
print(result)

from typing import Callable, Dict


def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)

    return apply_discount


# Створення словника з функціями знижок
discount_functions: Dict[str, Callable] = {
    "10%": discount(10),
    "12%": discount(12),
    "20%": discount(20),
    "30%": discount(30),
}

# Використання функції зі словника
price = 500
discount_type = "12%"

discounted_price = discount_functions[discount_type](price)
print(f"Ціна зі знижкою {discount_type}: {discounted_price}")

# Dictionary comprehensions
sq = {x: x**2 for x in range(1, 10)}
print(sq)


sq_dict = {x: x**2 for x in range(1, 10) if x > 5}
print(sq_dict)

# lambda arguments: expression
# print((lambda x, y: x + y)(4, 4))

numbers = [1, 2, 3, 4, 5, 6, 7]

for i in map(lambda x: x**2, numbers):
    # print(i)
    sq_numbers = list(map(lambda x: x**2, numbers))
print(sq_numbers)
"""


nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums)
