import os
from dotenv import load_dotenv
from getpass import getpass
from cryptography.fernet import Fernet
import csv
import re


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    return bool(match)
    


def add_user_info():
    encryption_key = os.getenv("KEY")
    email_id = input("Enter email id: ")
    if is_valid_email(email_id):
        print("Great! Valid email address....")   

        password = getpass("Enter password: ")

        encrypted_password = encrypt_data(encryption_key, password)
        csv_file_path = "UserData/userdata.csv"

        with open(csv_file_path, "a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([email_id, encrypted_password])

        print("User added succesfully!! ")
    else:
            print("Invalid email address.")

def generate_key():
    encryption_key = os.getenv("KEY")

    if not encryption_key:
        new_key_value = Fernet.generate_key()
        os.environ["KEY"] = new_key_value.decode()
        with open(".env", "a") as env_file:
            env_file.write(f"KEY={new_key_value.decode()}\n")
        print("Generated Key")
    else:
        print("Key Found")

# Encrypt data
def encrypt_data(encryption_key, data):
    f = Fernet(encryption_key.encode())
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data.decode()

# Decrypt data
def decrypt_data(encryption_key , encrypted_data):
    f = Fernet(encryption_key.encode())
    decrypted_data = f.decrypt(encrypted_data.encode())
    return decrypted_data.decode()
def get_key():
    return os.getenv("KEY")
def add_user():
    load_dotenv()
    generate_key()
    add_user_info()
load_dotenv()
