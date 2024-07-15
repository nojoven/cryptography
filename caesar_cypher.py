import string

def generate_the_alphabet_string():
    # Generate the str of letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = string.ascii_uppercase
    return letters

def generate_key(shift_number, letters):
    print(shift_number)
    key = {}
    count = 0
    for char in letters:
        # Dont forget the modulo to avoid out of range index error
        key[char] = letters[(count + shift_number) % len(letters)]
        count += 1
        # print(count)
        # print(key)
    return key


def encrypt(key, message_to_encrypt):
    # cipher AKA the encrypted message
    cipher = ""
    for char in message_to_encrypt:
        if char in key:
            cipher += key[char]
        else:
            cipher += char
    return cipher

def decrypt(decryption_key, cipher):
    return encrypt(decryption_key, cipher)

if __name__ == "__main__":
    shift_number = 3
    print(f"This caesar cipher will use a shift number of {shift_number}")
    letters = generate_the_alphabet_string()
    print(f"Our alphabet is contains {len(letters)} letters : {letters}")

    key = generate_key(shift_number, letters)
    print(f"The key is {key}")

    message_to_encrypt = "YOU ARE AWESOME!"
    print(f"Message to encrypt is '{message_to_encrypt}'")
    encryption_result = encrypt(key, message_to_encrypt)
    print(f"Result of encryption is {encryption_result}")

    len_of_decryption_key = len(letters) - shift_number
    print(f"Lengh of decryption key is {len_of_decryption_key}")

    decryption_key = generate_key(len(letters)-shift_number, letters)
    print(f"Decription key is {decryption_key}")

    decrypted_message = decrypt(decryption_key, "BRX DUH DZHVRPH!")
    print(f"Decrypted message is {decrypted_message}")

    assert decrypted_message == message_to_encrypt

    print(f"{message_to_encrypt} == {decrypted_message}")


