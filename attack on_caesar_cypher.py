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


def get_decryption_key(key):
    dkey = {}
    for char in key:
        dkey[key[char]] = char
    return dkey

if __name__ == "__main__":
    shift_number = 3
    print(f"This caesar cipher will use a shift number of {shift_number}")
    letters = generate_the_alphabet_string()
    print(f"Our alphabet is contains {len(letters)} letters : {letters}")

    # This is done by our ennemy
    # The key is the dict that maps each letter to another one on shift
    key = generate_key(shift_number, letters)
    print(f"The key is {key} ({len(key)} key-value pairs)")

    message_to_encrypt = "YOU ARE AWESOME!"
    print(f"Message to encrypt is '{message_to_encrypt}'")

    # The result of the encryption, also called cipher
    encryption_result = encrypt(key, message_to_encrypt)
    print(f"Result of encryption is {encryption_result}")


    # This is us trying to break their cipher
    for i in range(26):
        # There are 26 letters is our alphabet
        # So there are 26 items in key (it's a dict)
        dkey = generate_key(i, letters)
        message = encrypt(dkey, encryption_result)
        print(message)
        if message == message_to_encrypt:
            print(f"We only need {i} attempts to find a meaningful text: '{message}'")
            print("We broke through their defense!")
            break



