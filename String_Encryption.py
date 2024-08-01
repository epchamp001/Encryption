from cryptography.fernet import Fernet

def write_key():
    # Generates a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Loads the key form the current directory named 'key.key'

    return open("key.key", "rb").read()

# generate and write a new key
write_key()
# load the previously generated key
key = load_key()




# String encryption
message = "some secret message".encode()

# initialize the Fernet class
f = Fernet(key)

# encrypt the message
encrypted = f.encrypt(message)

print(encrypted)

# decrypt
decrypted_encrypted = f.decrypt(encrypted)
print(decrypted_encrypted)




