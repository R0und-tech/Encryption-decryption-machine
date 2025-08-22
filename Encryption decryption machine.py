import random

def generate_key_func(length):
    """
    генерация ключа по длине слова
    """
    #Русские буквы в нижнем / верхнем регистре
    russian_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    russian_letters = russian_letters.upper()
    if length <= 0:
        return "Длина должна быть положительным числом"
    key_word = ''.join(random.choice(russian_letters) for _ in range(length))
    return key_word.upper()

def binary_key_word_func(key_word):
    """
    перевод сгенерированного ключа в двоичное значение
    """
    binary_key_word = ''
    for char in key_word:
        for byte in char.encode('utf-8'):
            binary_key_word += f'{byte:08b}'
    return binary_key_word

def binary_original_word(original_word):
    """
    перевод введенного слова в двоичное значение
    """
    binary_original_word = ''
    for char in original_word:
        for byte in char.encode('utf-8'):
            binary_original_word += f'{byte:08b}'
    return binary_original_word

def length(binary_original_word, binary_key_word):
    """
    выравнивание двоичных значений слова и ключа по длине
    """
    max_length = max(len(binary_original_word), len(binary_key_word))
    binary_original_word = binary_original_word.zfill(max_length)
    binary_key_word = binary_key_word.zfill(max_length)
    return (binary_original_word, binary_key_word)

def encrypt_func(b_o_w, b_k_w, m_l):
    """
    операция XOR (побитового сложения значений слова и ключа)
    """
    encrypted_result = ""
    for byte in range(m_l):
        if b_o_w[byte] != b_k_w[byte]:
            encrypted_result += "1"
        else:
            encrypted_result += "0"
    return encrypted_result




original_word = input().upper()
length = len(original_word)
key_word = generate_key_func(length)
bin_key_word = binary_key_word_func(key_word)
bin_original_word = binary_original_word(original_word)
print(key_word)
print(bin_key_word)
print(original_word)
print(bin_original_word)



