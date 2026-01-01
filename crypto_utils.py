
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from logger import log_action

def derive_key(master_password: str) -> bytes:
    password_bytes = master_password.encode()
    salt = b"statit_salt_for_now"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),      # Modern hash
        length=32,      # Key length
        salt=salt,
        iterations=100_000,     # Protection from brute force
    )
    key = kdf.derive(password_bytes)      # Password -> crypto key
    return base64.urlsafe_b64encode(key)

def generate_key():      # Create secret key
    key = Fernet.generate_key()     # Generate random key in bytes
    with open("secret.key", "wb") as f:
        f.write(key)
        return key


def load_key():
    with open("secret.key", "rb") as f:
        return f.read()
    

def encrypt_password(session_key, password):        
    fernet = Fernet(session_key)    # Create object that know how to encrypt
    encrypted = fernet.encrypt(password.encode())       # Password.encode() -> text into bytes
    return encrypted.decode()       # .decode() => bytes -> text


def decrypt_password(session_key, encrypted_password, username="admin"):
    fernet = Fernet(session_key)
    try:
        decrypted = fernet.decrypt(encrypted_password.encode())  
        return decrypted.decode()
    except InvalidToken:
        log_action(username, "DECRYPT_FAILED")
        return None
