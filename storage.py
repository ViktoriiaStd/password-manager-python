from crypto_utils import encrypt_password
from crypto_utils import decrypt_password
from logger import log_action

def add_password(session_key, service_name, service_password, username="admin"):
    encrypted_password = encrypt_password(session_key, service_password)
    try:
        with open(r"C:\Users\admin\Desktop\Password_Manager\passwords.txt", "a") as f:
            f.write(f"{service_name.lower()}: {encrypted_password}\n")
            log_action(username, "ADD_PASSWORD", service_name)
            return {"status": "success", "data": None}
    except FileNotFoundError:
        log_action(username, "ADD_PASSWORD_FILE_ERROR", service_name)
        return {"status": "file_error", "data": None}

def view_passwords(session_key, username="admin"):
    try:
        with open(r"C:\Users\admin\Desktop\Password_Manager\passwords.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                 return {"status": "empty", "data": None}
            # Max service name length
            max_len = max(len(line.split(": ")[0]) for line in lines)
            result = []

            for i, line in enumerate(lines, start=1):
                service, password = line.strip().split(": ")
                decrypted_password = decrypt_password(session_key, password)

                if decrypted_password is None:
                    hidden_pass = "[DECRYPT ERROR]"
                else:
                    hidden_pass = decrypted_password[:2] + "*" * (len(decrypted_password) - 2)
                result.append((f"{i}. {service.ljust(max_len)} : {hidden_pass}"))
        log_action(username, "VIEW_PASSWORDS_SUCCESS")
        return {"status": "success", "data": result}
            
    except FileNotFoundError:
        log_action(username, "VIEW_PASSWORD_FILE_ERROR")
        return {"status": "file_error", "data": None}
              

def find_password(session_key, service_name, username="admin"):
    try:
        with open(r"C:\Users\admin\Desktop\Password_Manager\passwords.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                return {"status": "empty", "data": None}
            for line in lines:
                service, password = line.strip().split(": ")
                if service == service_name.lower():
                    log_action(username, "FIND_PASSWORD_SUCCESS", service_name)
                    
                    decrypted_password = decrypt_password(session_key, password)
                    
                    if decrypted_password is None:
                        log_action(username, "FIND_PASSWORD_DECRYPT_FAILED", service_name)
                        return  {"status": "decrypt_error", "data": None}
                    
                    hidden_pass = decrypted_password[:2] + "*" * (len(decrypted_password) - 2)
                    log_action(username, "FIND_PASSWORD_SUCCESS", service_name)
                    return {"status": "success", "data" : hidden_pass}
            log_action(username, "FIND_PASSWORD_NOT_FOUND", service_name)
            return {"status": "not_found", "data": None}
        
    except FileNotFoundError:
        log_action(username, "FIND_PASSWORD_FILE_ERROR")
        return {"status": "file_error", "data": None}
            

def delete_password(service_name, username="admin"):
    try:
        with open(r"C:\Users\admin\Desktop\Password_Manager\passwords.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                return {"status": "empty", "data": None}
            found = False
            temp_pass_list = []
            for line in lines:
                service, _ = line.strip().split(": ")
                if service == service_name.lower():
                    found = True
                else:
                    temp_pass_list.append(line)

            if found:
                    with open(r"C:\Users\admin\Desktop\Password_Manager\passwords.txt", "w") as f:
                        f.writelines(temp_pass_list)
                    log_action(username, "DELETE_PASSWORD_SUCCESS", service_name)
                    return {"status": "deleted", "data": None}
            else:
                log_action(username, "DELETE_PASSWORD_NOT_FOUND", service_name)
                return {"status": "not_found", "data": None}
                        
    except FileNotFoundError:
        log_action(username, "DELETE_PASSWORD_FILE_ERROR")
        return {"status": "file_error", "data": None}



