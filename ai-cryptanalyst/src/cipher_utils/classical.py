# src/cipher_utils/classical.py

def caesar_encrypt(text, shift):
    result = []
    for char in text.upper():
        if char.isalpha():
            result.append(chr((ord(char) - 65 + shift) % 26 + 65))
        else:
            result.append(char)
    return ''.join(result)

def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()
    key_extended = ''.join(key[i % len(key)] for i in range(len(text)))
    result = []
    for t_char, k_char in zip(text, key_extended):
        if t_char.isalpha():
            shift = ord(k_char) - 65
            result.append(chr((ord(t_char) - 65 + shift) % 26 + 65))
        else:
            result.append(t_char)
    return ''.join(result)

def rail_fence_encrypt(text, num_rails):
    if num_rails == 1:
        return text
    rail = ['' for _ in range(num_rails)]
    direction = False
    row = 0
    for char in text:
        rail[row] += char
        if row == 0 or row == num_rails - 1:
            direction = not direction
        row += 1 if direction else -1
    return ''.join(rail)

def columnar_transposition_encrypt(text, key):
    text = text.replace(" ", "")
    n_cols = len(key)
    sorted_key = sorted(list(enumerate(key)), key=lambda x: x[1])
    columns = ['' for _ in range(n_cols)]

    for idx, char in enumerate(text):
        col = idx % n_cols
        columns[col] += char

    cipher_text = ''
    for i, _ in sorted_key:
        cipher_text += columns[i]
    return cipher_text
