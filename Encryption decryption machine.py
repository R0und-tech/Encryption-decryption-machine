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
    binary_key_word = ''
    for char in key_word:
        for byte in char.encode('utf-8'):
            binary_key_word += f'{byte:08b}'
    return binary_key_word

def binary_original_word(original_word):
    binary_original_word = ''
    for char in original_word:
        for byte in char.encode('utf-8'):
            binary_original_word += f'{byte:08b}'
    return binary_original_word



def encrypt_func(binary_original_word, binary_key_word):
    ...


original_word = input().upper()
length = len(original_word)
key_word = generate_key_func(length)
bin_key_word = binary_key_word_func(key_word)
bin_original_word = binary_original_word(original_word)
print(key_word)
print(bin_key_word)
print(original_word)
print(bin_original_word)



