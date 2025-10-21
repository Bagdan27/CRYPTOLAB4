import numpy as np

# 1. Алфавіт згідно з таблицею 4.1
alphabet = [
    'а', 'б', 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'й', 'к', 'л', 'м', 'н',
    'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я'
]
mod = len(alphabet)

#  2. Допоміжні функції

def letter_to_num(ch):
    return alphabet.index(ch)

def num_to_letter(num):
    return alphabet[num % mod]

def text_to_vector(text):
    return [letter_to_num(ch) for ch in text.lower() if ch in alphabet]

def vector_to_text(vec):
    return ''.join(num_to_letter(num) for num in vec)

def mod_inverse(a, m):

    t, new_t = 0, 1
    r, new_r = m, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError("Елемент не має оберненого")
    if t < 0:
        t += m
    return t

def matrix_mod_inverse(matrix, m):
    det = int(round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det % m, m)
    matrix_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)
    ) % m
    return matrix_inv.astype(int)

#  3. Формування матриці ключа з прізвища

surname = "Аністратенко".lower()
surname_nums = text_to_vector(surname)


while len(surname_nums) < 9:
    surname_nums.append(letter_to_num('ь'))

key_matrix = np.array(surname_nums[:9]).reshape(3, 3)
print("Ключова матриця H1:")
print(key_matrix)

# 4. Функції шифрування та дешифрування

def hill_encrypt(plaintext, key, m):
    plaintext_nums = text_to_vector(plaintext)
    while len(plaintext_nums) % 3 != 0:
        plaintext_nums.append(letter_to_num('ь'))

    ciphertext = []
    for i in range(0, len(plaintext_nums), 3):
        block = np.array(plaintext_nums[i:i+3])
        enc_block = np.dot(key, block) % m
        ciphertext.extend(enc_block)
    return vector_to_text(ciphertext)

def hill_decrypt(ciphertext, key, m):
    key_inv = matrix_mod_inverse(key, m)
    ciphertext_nums = text_to_vector(ciphertext)
    plaintext = []
    for i in range(0, len(ciphertext_nums), 3):
        block = np.array(ciphertext_nums[i:i+3])
        dec_block = np.dot(key_inv, block) % m
        plaintext.extend(dec_block)
    return vector_to_text(plaintext)

# 5. Приклад

plaintext = "богдан"
ciphertext = hill_encrypt(plaintext, key_matrix, mod)
decrypted = hill_decrypt(ciphertext, key_matrix, mod)

print("\nВідкритий текст:", plaintext)
print("Зашифрований текст:", ciphertext)
print("Розшифрований текст:", decrypted)
