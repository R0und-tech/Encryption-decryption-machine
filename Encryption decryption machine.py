import random

def generate_key_func(length, language):
    """
    генерация ключа по длине слова

    """
    if language == "rus":
        #Русские буквы в нижнем / верхнем регистре
        russian_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        russian_letters = russian_letters.upper()
        if length <= 0:
            return "Длина должна быть положительным числом"
        key_word = ''.join(random.choice(russian_letters) for _ in range(length))
        return key_word.upper()
    if language == "eng":
        #Латинские буквы в нижнем / верхнем регистре
        latin_letters = 'abcdefghijklmnopqrstuvwxyz'
        latin_letters = latin_letters.upper()
        if length <= 0:
            return "Length should be a positive number"
        key_word = ''.join(random.choice(latin_letters) for _ in range(length))
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

def leng(binary_original_word, binary_key_word):
    """
    выравнивание двоичных значений слова и ключа по длине

    """
    max_length = max(len(binary_original_word), len(binary_key_word))
    binary_original_word = binary_original_word.zfill(max_length)
    binary_key_word = binary_key_word.zfill(max_length)
    return (binary_original_word, binary_key_word, max_length)

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


def main_ui():
    language_request = input("###Введи язык на котором ты будешь писать / Write down a language in which you will work###\nRus/Eng:").lower()
    original_word = input("###Введи слово или фразу, которое хочешь закодировать / Write down a word or phrase which you want to encode###").lower()
    length = len(original_word)
    key_word = generate_key_func(length, language_request)
    bin_key_word = binary_key_word_func(key_word)
    bin_original_word = binary_original_word(original_word)
    b_o_w, b_k_w, m_l = leng(bin_key_word, bin_original_word)
    encrypted_word = encrypt_func(b_o_w, b_k_w, m_l)
    print(f"###Это зашифрованное слово или фраза / This is encrypted word or phrase: {encrypted_word}###")
    print(f"###Это ключ-слово / This is a key word: {key_word}###")


main_ui()




