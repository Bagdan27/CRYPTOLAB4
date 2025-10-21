import numpy as np

#  Функція множення за модулем
def multiply_mod(a, b, mod):

    return (a * b) % mod


#  Функція знаходження оберненого елемента у простому полі
def mod_inverse(a, mod):

    t, new_t = 0, 1
    r, new_r = mod, a

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        raise ValueError(f"{a} не має оберненого елемента за модулем {mod}")
    if t < 0:
        t += mod

    return t


#  Функція знаходження оберненої матриці у простому полі
def matrix_mod_inverse(matrix, mod):

    det = int(round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det % mod, mod)

    matrix_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)
    matrix_inv = np.mod(matrix_inv, mod)

    return matrix_inv


# Приклад використання
if __name__ == "__main__":
    mod = 29
    a, b = 7, 5

    print("Множення за модулем:", multiply_mod(a, b, mod))
    print("Обернений елемент:", mod_inverse(a, mod))

    matrix = np.array([[3, 10], [20, 9]])
    print("Початкова матриця:")
    print(matrix)

    inv_matrix = matrix_mod_inverse(matrix, mod)
    print("Обернена матриця за модулем", mod, ":")
    print(inv_matrix)
