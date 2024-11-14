def generate_vigenere_table():
    """Генерация таблицы Виженера."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = []
    for i in range(len(alphabet)):
        shifted_alphabet = alphabet[i:] + alphabet[:i]
        table.append(shifted_alphabet)
    return table


def vigenere_encrypt(plain_text, key):
    """Шифрование текста с использованием шифра Виженера."""
    table = generate_vigenere_table()
    encrypted_text = ""
    key = key.upper()
    key_len = len(key)

    for i, char in enumerate(plain_text.upper()):
        if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            encrypted_text += char  # Пропускаем символы, не входящие в алфавит
            continue
        row = ord(key[i % key_len]) - ord('A')  # Строка определяется ключом
        col = ord(char) - ord('A')  # Столбец определяется символом текста
        encrypted_text += table[row][col]
    return encrypted_text


def vigenere_decrypt(encrypted_text, key):
    """Дешифрование текста с использованием шифра Виженера."""
    table = generate_vigenere_table()
    decrypted_text = ""
    key = key.upper()
    key_len = len(key)

    for i, char in enumerate(encrypted_text.upper()):
        if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            decrypted_text += char  # Пропускаем символы, не входящие в алфавит
            continue
        row = ord(key[i % key_len]) - ord('A')  # Строка определяется ключом
        col = table[row].index(char)  # Находим символ в строке
        decrypted_text += chr(col + ord('A'))
    return decrypted_text


# Основной код
if __name__ == "__main__":
    # Ввод данных от пользователя
    plain_text = input("Введите текст для шифрования: ")
    key = input("Введите ключ: ")

    # Шифрование
    encrypted_text = vigenere_encrypt(plain_text, key)
    print(f"Зашифрованный текст: {encrypted_text}")

    # Дешифрование
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print(f"Расшифрованный текст: {decrypted_text}")





