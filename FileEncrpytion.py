Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Helper function to pad data to a multiple of 16 bytes for AES encryption
def pad(data):
    while len(data) % 16 != 0:
        data += b' '
    return data

# Function to generate a secure 256-bit key for AES encryption
def generate_key():
    return get_random_bytes(32)

# Save the generated key to a specified file
def save_key(key, filename):
    with open(filename, 'wb') as file:
        file.write(key)

# Load an encryption key from a specified file
def load_key(filename):
    with open(filename, 'rb') as file:
        return file.read()

# Encrypt the contents of a file using the provided key
def encrypt_file(filename, key):
    with open(filename, 'rb') as file:
        data = file.read()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(data))
    with open(filename + '.enc', 'wb') as file:
        file.write(encrypted_data)

# Decrypt an encrypted file using the provided key
def decrypt_file(filename, key):
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data).rstrip(b' ')
    decrypted_filename = filename.replace('.enc', '')
    with open(decrypted_filename, 'wb') as file:
        file.write(decrypted_data)

# Main application class for the GUI
def EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" Encryption & Decryption Application")

        # Instruction label at the top of the app
        tk.Label(root, text="Choose an option below:", font=("Arial", 12), bg="lightgreen", fg="black").pack(pady=10)

        # Buttons for each functionality: key generation, encryption, and decryption
        tk.Button(root, text="Generate Key", command=self.generate_key, width=20, bg="black", fg="white").pack(pady=5)
        tk.Button(root, text="Encrypt File", command=self.encrypt_file, width=20, bg="black", fg="white").pack(pady=5)
...         tk.Button(root, text="Decrypt File", command=self.decrypt_file, width=20, bg="black", fg="white").pack(pady=5)
... 
...     def generate_key(self):
...         key = generate_key()
...         save_path = filedialog.asksaveasfilename(
...             defaultextension=".key", filetypes=[("Key Files", "*.key")]
...         )
...         if save_path:
...             save_key(key, save_path)
...             messagebox.showinfo("Success", f"Key saved to {save_path}")
... 
...     def encrypt_file(self):
...         key_path = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
...         if key_path:
...             key = load_key(key_path)
...             file_path = filedialog.askopenfilename()
...             if file_path:
...                 encrypt_file(file_path, key)
...                 messagebox.showinfo("Success", "File encrypted successfully!")
... 
...     def decrypt_file(self):
...         key_path = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
...         if key_path:
...             key = load_key(key_path)
...             file_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.enc")])
...             if file_path:
...                 decrypt_file(file_path, key)
...                 messagebox.showinfo("Success", "File decrypted successfully!")
... 
... # Run the application
... if __name__ == "__main__":
...     root = tk.Tk()
...     app = EncryptionApp(root)
...     root.mainloop()
