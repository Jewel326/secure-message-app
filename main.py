import rsa
import os

# Create directories if not present
os.makedirs("keys", exist_ok=True)
os.makedirs("messages", exist_ok=True)

def generate_keys():
    public_key, private_key = rsa.newkeys(2048)
    with open("keys/public.pem", "wb") as pub_file:
        pub_file.write(public_key.save_pkcs1("PEM"))
    with open("keys/private.pem", "wb") as priv_file:
        priv_file.write(private_key.save_pkcs1("PEM"))
    print("\n✅ RSA Key Pair generated successfully and saved in 'keys/' folder.")

def encrypt_message(message):
    try:
        with open("keys/public.pem", "rb") as pub_file:
            public_key = rsa.PublicKey.load_pkcs1(pub_file.read())
        encrypted = rsa.encrypt(message.encode(), public_key)
        with open("messages/encrypted.txt", "wb") as enc_file:
            enc_file.write(encrypted)
        print("\n🔒 Message encrypted and saved to 'messages/encrypted.txt'.")
    except FileNotFoundError:
        print("\n⚠️ Public key not found. Please generate keys first.")

def decrypt_message():
    try:
        with open("keys/private.pem", "rb") as priv_file:
            private_key = rsa.PrivateKey.load_pkcs1(priv_file.read())
        with open("messages/encrypted.txt", "rb") as enc_file:
            encrypted = enc_file.read()
        decrypted = rsa.decrypt(encrypted, private_key).decode()
        with open("messages/decrypted.txt", "w") as dec_file:
            dec_file.write(decrypted)
        print("\n🔓 Message decrypted and saved to 'messages/decrypted.txt'.")
    except FileNotFoundError:
        print("\n⚠️ Required files not found. Please ensure encryption has been done and keys exist.")
    except rsa.DecryptionError:
        print("\n❌ Decryption failed. The data may be corrupted or the keys may not match.")

def menu():
    while True:
        print("\n🎛️  Secure Message CLI Menu")
        print("1. Generate RSA Key Pair")
        print("2. Encrypt a Message")
        print("3. Decrypt a Message")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            generate_keys()
        elif choice == '2':
            message = input("\n📝 Enter message to encrypt: ")
            encrypt_message(message)
        elif choice == '3':
            decrypt_message()
        elif choice == '4':
            print("\n👋 Exiting the app. Stay secure!")
            break
        else:
            print("\n❌ Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    menu()
