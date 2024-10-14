import string


def encrypt(message, key):
    if not isinstance(key, int) or key <= 0 or key > 25:
        raise ValueError("Key must be an integer between 1 and 25")

    encrypted_message = ""

    for character in message:
        if character in string.ascii_uppercase:
            encrypted_message += chr((ord(character) + key - 65) % 26 + 65)
        elif character in string.ascii_lowercase:
            encrypted_message += chr((ord(character) + key - 97) % 26 + 97)
        else:
            encrypted_message += character

    return encrypted_message

def decrypt(message, key):
    if not isinstance(key, int) or key <= 0 or key > 25:
        raise ValueError("Key must be an integer between 1 and 25")

    decrypted_message = ""

    for character in message:
        if character in string.ascii_uppercase:
            decrypted_message += chr((ord(character) - key - 65) % 26 + 65)
        elif character in string.ascii_lowercase:
            decrypted_message += chr((ord(character) - key - 97) % 26 + 97)
        else:
            decrypted_message += character

    return decrypted_message

def break_crypt(message):
    for key in range(1,26):
        possible_message = decrypt(message, key)
        print(f"Key {key}: {possible_message}")

def get_key():
    while True:
        try:
            key = int(input("Input the key (an integer between 1 and 25):"))
            if 1 <= key <= 25:
                return key
            else:
                print("Key must be between 1 and 25.")
        except ValueError:
            print("Please input a valid integer.")

def get_message():
    return input("input the message: ")

def action():

    while True:
        print('\nwhat would you like to do? ')
        choice = input("e: encrypt\nd: decrypt\nb: break\nq: quit\n>")

        if choice.lower() == 'q':
            print("Quitting program, bye!")
            break

        elif choice.lower() == 'd':
            key = get_key()
            message = get_message()
            plaintext = decrypt(message, key)
            print("The decrypted message is %s" % plaintext)

        elif choice.lower() == 'e':
            key = get_key()
            message = get_message()
            cryptotext = encrypt(message, key)
            print("The encrypted message is %s" %cryptotext)

        elif choice.lower() == 'b':
            message = get_message()
            break_crypt(message)

        else:
            print("invalid choice.")

if __name__== "__main__":
    action()