# 🔐 Secure Message App (CLI)

This is a beginner-friendly command-line Python application that allows you to **encrypt** and **decrypt** text messages using **RSA encryption**. Built as a cybersecurity learning project to explore the fundamentals of public-key cryptography.

---

## ✨ Features

- ✅ Generate RSA key pairs (2048-bit)
- 🔒 Encrypt plain text messages
- 🔓 Decrypt encrypted messages
- 🗃 Organized output files
- 📟 Interactive CLI menu

---

## 📂 Project Structure
secure-message-app/
-keys/ Stores public and private RSA keys
-messages/ Stores encrypted and decrypted message files
-main.py Main CLI application
-README.md This file


---

## 🧠 Concepts Practiced

- Asymmetric encryption (RSA)
- Public and private key generation
- Secure message handling
- Command-line interface (CLI) logic
- Python file handling

---

## 🛠 Requirements

- Python 3.7+
- [`rsa`](https://pypi.org/project/rsa/) Python library

To install required package:

```bash
pip install rsa 

---

THE STEPS
STEP 1 - Clone or download my repo
git clone https://github.com/Jewel326/secure-message-app.git
cd secure-message-app

STEP 2 - Run the application
python main.py (in your terminal)

Step 3 - Use the CLI menu, you will see;
🎛️  Secure Message CLI Menu
1. Generate RSA Key Pair
2. Encrypt a Message
3. Decrypt a Message
4. Exit

Output files:
Encrypted messages: messages/encrypted.txt
Decrypted messages: messages/decrypted.txt
Keys: keys/public.pem keys/private.pem
 I added a ".gitignore" to prevent committing sensitive/generated files

venv/
__pycache__/
*.pyc
messages/*.txt
keys/*.pem
---

 As a cybersecurity enthusiast, I worked on this project to have a better understanding of cryptography fundamentals and how encryption works beyond theory (hands-on exercise with Python, keys and terminal logic). It's simple but powerful.





