# ALPHABET = {"А": 00000, "Б": 00001, "В": 00010, "Г": 000011, "Д": 00100, "Е": 00101, "Ж": 00110, "З": 00111, "И": 01000, "Й": 01001, "К": 01010, "Л": 01011, "М": 01100, "Н": 01101, "О": 01110, "П": 01111, "Р": 10000, "С": 10001, "Т": 10010, "У": 10011, "Ф": 10100, "Х": 10101, "Ц": 10110, "Ч": 10111, "Ш": 11000, "Щ": 11001, "Ъ": 11010, "Ы": 11011, "Ь": 11100, "Э": 11101, "Ю": 11110, "Я": 11111}

import random

def generate_key_func(length):
    # Русские буквы в нижнем / верхнем регистре
    russian_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    russian_letters = russian_letters.upper()
    if length <= 0:
        return "Длина должна быть положительным числом"
    key_word = ''.join(random.choice(russian_letters) for _ in range(length))
    return key_word.upper()

def binary_key_word_func(key_word):
    binary = ' '.join(format(ord(i), '08b') for i in key_word)
    return binary
    # for char in key_word:
    #     binary_key_word = bin(ord(char))[2:]
    #     print(binary_key_word)

def binary_original_word(original_word):
    ...


def encrypt_func(original_word, key):
    ...


original_word = input().upper()
length = len(original_word)
key_word = generate_key_func(length)
bin_key_word = binary_key_word_func(key_word)
print(key_word)
print(bin_key_word)

