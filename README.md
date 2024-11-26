# 🔒 Encryption Project
This Python project provides simple tools for encrypting and decrypting files and strings. The encryption is powered by the `cryptography` library, ensuring secure and reliable operations.

## ✨ Features
* 🛠 **File Encryption**: Encrypt and decrypt files with or without a password.
* 🔑 **String Encryption**: Encrypt and decrypt string data using generated keys.
* 🔐 **Custom Password Support**: Derive encryption keys using passwords and salts.
* 🖥 **Command-Line Interface**: Easily encrypt/decrypt files using CLI arguments.

## 📂 Files and Scripts
### 1. File_Encryption.py
* 🛠 **Purpose**: Provides basic file encryption and decryption functionality using a pre-generated key.
* 🔑 **Key Functions**:
  * `write_key`: Generates and saves a new encryption key.
  * `load_key`: Loads the key from the file `key.key`.
  * `encrypt`: Encrypts a given file.
  * `decrypt`: Decrypts a given file.
* 📋 **Example Usage**:
```python
key = load_key()
encrypt("data.csv", key)
decrypt("data.csv", key)
```

### 2. File_Encryption_with_Password.py
* 🛠 **Purpose**: Enhances file encryption by supporting password-based key derivation.
* 🔐 **Key Features**:
  * Password-based key generation with salt (`generate_key`).
  * Command-line arguments for encryption and decryption.
* 🖥 **Usage**:
```bash
python File_Encryption_with_Password.py data.csv -e  # Encrypt
python File_Encryption_with_Password.py data.csv -d  # Decrypt
```
* ⚙ **Arguments**:
  * `-e`: Encrypt the file.
  *  `-d`: Decrypt the file.
  * `--salt-size`: Set custom salt size for key derivation.

### 3. String_Encryption.py
* 🛠 **Purpose**: Demonstrates encrypting and decrypting strings using a generated key.
* 🔑 **Key Functions**:
  * Encrypts a string with `f.encrypt()`.
  * Decrypts a string with `f.decrypt()`.
### 📁 Additional Files:
**data.csv**: Sample file for encryption and decryption.
**key.key**: Stores the encryption key.
**salt.salt**: Stores the salt for password-based key derivation.
## 🧰 Installation
1. Clone the repository:
```bash
git clone <repository-url>
```
2. Install required dependencies:
```bash
pip install cryptography
```

## 🚀 How to Use
### 🔐 File Encryption
1. Generate a key (if needed):
```bash
write_key()
```
2. Encrypt the file:
```bash
encrypt("data.csv", key)
```
3. Decrypt the file:
```bash
decrypt("data.csv", key)
```

### 🔑 Password-Based Encryption
1. Encrypt with password:
```bash
python File_Encryption_with_Password.py data.csv -e
```
2. Decrypt with password:
```bash
python File_Encryption_with_Password.py data.csv -d
```

## 📋 Requirements
* Python 3.6+
* `cryptography` library

## ⚠️ Notes
* Keep the `key.key` and `salt.salt` files secure; losing them will make decryption impossible.
* Ensure the password is remembered when using password-based encryption.


