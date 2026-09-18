# 🔐 Text Crypter

**Text Crypter** is a simple Python-based text encryption and decryption tool that allows users to create their own character replacement rules.

Instead of using a fixed encryption method, users can define **their own characters, letters, numbers, or special symbols** for encryption and decryption.

## ✨ Features

* 🔒 Encrypt text using custom character mappings
* 🔓 Decrypt encrypted text using reverse mappings
* 🔤 Supports alphabets and letters
* 🔢 Supports numbers
* 🔣 Supports special characters and symbols
* ⚙️ Users can define their own encryption characters
* 🔄 Uses a reverse dictionary for decryption
* 🐍 Built with Python
* 💻 Simple and beginner-friendly

## 🧠 How It Works

Text Crypter uses **two dictionaries**:

### 1. Encryption Dictionary

The first dictionary contains the original characters as **keys** and their replacement characters as **values**.

For example:

```python
encrypt_dict = {
    "A": "B",
    "B": "C",
    "C": "D"
}
```

If the user enters:

```text
ABC
```

The encrypted result will be:

```text
BCD
```

### 2. Decryption Dictionary

The second dictionary contains the **reverse mapping** of the encryption dictionary.

```python
decrypt_dict = {
    "B": "A",
    "C": "B",
    "D": "C"
}
```

So:

```text
BCD
```

can be converted back to:

```text
ABC
```

## 🎯 Custom Character Mapping

The main feature of Text Crypter is that the user is **not restricted to predefined characters**.

For example, users can create mappings such as:

```text
A → #
B → @
C → $
1 → %
2 → &
! → ?
```

This allows different types of characters and symbols to be used according to the user's requirements.

## 🚀 Example

### Input

```text
HELLO
```

Suppose the custom mapping contains:

```text
H → #
E → @
L → $
O → %
```

### Encrypted Output

```text
#@$$%
```

Using the reverse dictionary, the encrypted text can be converted back to:

```text
HELLO
```

## 🛠️ Technologies Used

* **Python**
* **Python Dictionaries**
* **String Manipulation**

No external libraries are required.

## 📂 Project Structure

```text
TextCrypter/
│
├── TextCrypter.py
└── README.md
```

> The Python filename can be changed according to your actual project structure.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/TextCrypter.git
```

### 2. Open the project folder

```bash
cd TextCrypter
```

### 3. Run the Python script

```bash
python TextCrypter.py
```

## ⚠️ Important Note

Text Crypter is a **learning/project implementation of character substitution**.

It should **not be considered secure modern cryptography** for protecting passwords, sensitive information, or confidential data.

For real-world security applications, use established cryptographic algorithms and libraries such as AES rather than a custom substitution system.

## 🎓 Purpose of the Project

This project was created to practice and demonstrate Python concepts such as:

* Dictionaries
* Key-value pairs
* Reverse dictionaries
* String manipulation
* Loops
* User input
* Conditional statements
* Basic encryption/decryption logic

## 🔮 Future Improvements

Possible improvements include:

* Add a graphical user interface (GUI)
* Add file encryption/decryption
* Add automatic key generation
* Add password-based encryption
* Support larger character sets
* Add validation for duplicate mappings
* Add command-line arguments
* Improve error handling

## 👨‍💻 Author

**Vishal Gupta**

---

⭐ If you find this project useful, consider giving the repository a star!
