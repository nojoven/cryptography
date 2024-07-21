import string

def generate_the_alphabet_string():
    # Generate the str of letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = string.ascii_uppercase
    return letters

def generate_key(shift_number, letters):
    print(shift_number)
    # We need the sequence of letters that corresponds to the shift number
    # Create a dict that maps each original letter to its targer letter
    key = {} # This is the dict
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
    # Create the cipher with the values of the key which is a dict
    for char in message_to_encrypt:
        if char in key:
            cipher += key[char]
        else:
            cipher += char
    return cipher

def decrypt(decryption_key, cipher):
    # Reuse the same logic than the enctypt function
    # This time the returned value is not a cipher. 
    # It's the original unencrypted message.
    return encrypt(decryption_key, cipher)


def get_decryption_key(key):
    # Let's do the opposite of the generate_key function
    # Create a dict which is the decryption key
    dkey = {}
    # Each key of dkey is a value of the received key (parameter of this function)
    # The value becomes the key
    for char in key:
        # Each value is the corresponding key in the received dict
        # The key becomes the value
        dkey[key[char]] = char
    # dkey contains key 
    return dkey

if __name__ == "__main__":
    shift_number = 3
    print(f"This caesar cipher will use a shift number of {shift_number}")
    letters = generate_the_alphabet_string()
    print(f"Our alphabet is contains {len(letters)} letters : {letters}")

    # This is done by our ennemy
    # The key is the dict that maps each letter to another one on shift
    key = generate_key(shift_number, letters)
    print(f"The key is {key}")

    message_to_encrypt = "YOU ARE AWESOME!"
    print(f"Message to encrypt is '{message_to_encrypt}'")

    # The result of the encryption, also called cipher
    encryption_result = encrypt(key, message_to_encrypt)
    print(f"Result of encryption is {encryption_result}")


    # This is us trying to break their cipher
    len_of_decryption_key = len(letters) - shift_number
    print(f"Lengh of decryption key is {len_of_decryption_key}")

    decryption_key = generate_key(len(letters)-shift_number, letters)
    print(f"Decription key is {decryption_key}")

    decrypted_message = decrypt(decryption_key, "BRX DUH DZHVRPH!")
    print(f"Decrypted message is {decrypted_message}")

    assert decrypted_message == message_to_encrypt

    print(f"{message_to_encrypt} == {decrypted_message}")

    print("Using the get_decryption_key function")
    dkey = get_decryption_key(key)
    print(f"dkay is {dkey}")

    cipher_to_decrypt = encryption_result
    original_message = encrypt(dkey, cipher_to_decrypt)
    print(f"Again, we find that the original message was {original_message}")
