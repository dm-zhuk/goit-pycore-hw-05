import collections
from collections import Counter, defaultdict, namedtuple, deque
from decimal import Decimal as d, getcontext

print(d("0.1") + d("0.2") == d("0.3"))
print(d("0.1") + d("0.2"))


getcontext().prec = 6
print(d("1") / d("7"))

getcontext().prec = 8
print(d("1") / d("7"))

"""
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
"""
