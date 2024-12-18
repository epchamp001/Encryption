from cryptography.fernet import Fernet

def write_key():
    # Generates a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Loads the key form the current directory named 'key.key'

    return open("key.key", "rb").read()

# File Encryption
def encrypt(filename, key):
    # Given a filename (str) and key (bytes), it encrypts the file and write it

    f = Fernet(key)

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()

    # encrypt data
    encrypted_data = f.encrypt(file_data)

    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    # Given a filename (str) and key (bytes), it decrypts the file and write it

    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

# write_key()

key = load_key()

file = "data.csv"

# encrypt(file, key)
decrypt(file, key)