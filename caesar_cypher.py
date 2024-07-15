import string
def generate_key(shift_number):
    print(shift_number)
    # Generate the str of letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = string.ascii_uppercase
    # print(letters)
    key = {}
    count = 0
    for char in letters:
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

if __name__ == "__main__":
    shift_number = 3
    key = generate_key(shift_number)
    print(f"The key is {key}")
    message_to_encrypt = "YOU ARE AWESOME!"
    encryption_result = encrypt(key, message_to_encrypt)
    print(encryption_result)


