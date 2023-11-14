from hashlib import sha256
import itertools

def key_cracking(hashed: str) -> str:
    characters = "abcdefghijklmnopqrstuvwxyz"

    for combination in itertools.product(characters, repeat=4):
        password = ''.join(combination)
        hash_attempt = sha256(password.encode()).hexdigest()

        if hash_attempt == hashed:
            return password

    return "Password not found"


# Verejné testy:
print(key_cracking("a746222f09d85605c52d4e636788d6ffdc274698b98b8c5f3244c06958683a69"))  # snow
print(key_cracking("e6ad06ca7b0a33fbb0ea8d52e482eacca927a5735101bd2a0712d2f230233089"))  # iglu
