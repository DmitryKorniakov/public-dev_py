### Задание 2.1: Таблица умножения

for i in range(1, 11):
    for j in range(1, 11):
        num = i * j
        print(f"{i:2} * {j:2} = {num:3}", end="  | ")
    print()

### Задание 2.2: Поиск простых чисел

limit = int(input('Введите значение, до какого числа будут выводиться простые числа:\n'))

def find_primes(n):
    primes = []
    for n1 in range(2, n + 1):
        for i in range(2, n1):
            if n1 % i == 0:
                break
        else:
            primes.append(n1)
    return primes

print(find_primes(limit))

### Задание 2.3: Игра "Угадай число"

import random

print('Постарайся отгадать число 1 до 100 за минимальное число попыток.\n')

# начальные значения
the_number = random.randint(1, 100)
guess = int(input('Baшe предположение: '))
tries = 1

# цикл отгадывания
while guess != the_number:
    if guess > the_number:
        print('Меньше')
        guess = int(input('Ваше предположение: '))
        tries += 1
    else:
        print('Больше')
        guess = int(input('Ваше предположение: '))
        tries += 1
print(f'Вам удалось отгадать число! Это в самом деле {the_number}')
print(f'Вы затратили на отгадывание всего лишь {tries} попыток!\n')

### Задание 2.4: Анализ текста

text = input('Введите текст на проверку\n')

# сбор данных из str
symbol_count = len(text)
words_count = text.count(' ') + 1
sentense_count = text.count('.') + text.count('!') + text.count('?')

print(f'В тексте {symbol_count} символов, {words_count} слов и {sentense_count} предложений')

words = text.lower().split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

sorted_words = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
print("Топ 5 слов:")
for word, count in sorted_words[:5]:
    print(f"{word}: {count}")

