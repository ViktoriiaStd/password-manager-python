import hashlib 
from crypto_utils import derive_key
import getpass
from logger import log_action
from validation import prompt_non_empty

MASTER_HASH_FILE = r"C:\Users\admin\Desktop\Password_Manager\master.hash"
MAX_ATTEMPTS = 3

def check_master_password(username="admin"):
    
    try: 
        with open(MASTER_HASH_FILE, "r") as f:
            stored_hash = f.read().strip()

    except FileNotFoundError:
        log_action(username, "LOGIN_ERROR", "master.hash missing")
        return None
    
    for attempt in range(1, MAX_ATTEMPTS + 1):
        password = getpass.getpass("Enter master password: ")
        entered_hash = hashlib.sha256(password.encode()).hexdigest()

        if entered_hash == stored_hash:
            log_action(username, "LOGIN_SUCCESS")
            return derive_key(password)
        
        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            log_action(username, "LOGIN_FAILED" f"attempt {attempt}")
            print(f"Wrong password. Attempts left: {remaining}")

    log_action(username, "LOGIN_LOCKED", "too many attempts")
    print("Too many failed attempts. Exiting.")
    return None