
from auth import check_master_password
from storage import add_password, view_passwords, find_password, delete_password
from validation import validate_password, prompt_non_empty

def main():
    session_key = check_master_password()
    if not session_key:
        print("Access denied. Exiting.")
        return
    print("Access granted")

    while True:
        print("\n=== PASSWORD MANAGER MENU ===")
        print("1. Add password")
        print("2. View passwords")
        print("3. Find password")
        print("4. Delete password")
        print("5. Exit")

        try:
            choice = int(input("Choose an option: "))   
        except ValueError:
            print("Invalid input. Enter a number between 1-5.")
            continue

        if choice == 1:
            print(" ")
            print("--- ADD PASSWORD ---")
            service_name = prompt_non_empty("Enter service name: ")

            while True:
                service_password = prompt_non_empty("Enter password: ")
                
                errors = validate_password(service_password)
                if errors:
                    print("\nInvalid password:")
                    for error in errors:
                        print(error)
                    print()
                    continue
                break


            status = add_password(session_key, service_name, service_password)
            if status["status"] == "success":
                print("Password added successfully")
            elif status["status"] == "file_error":
                print("File not found. Cannot add password.")
            
        elif choice == 2:
            print(" ")
            print("--- VIEW PASSWORDS ---")
            status = view_passwords(session_key)
            if status["status"] == "success":
                for line in status["data"]:
                    print(line)
            elif status["status"] == "empty":
                print("No passwords stored yet.")
            elif status["status"] == "file_error":
                print("File not found. Cannot view passwords.")

        elif choice == 3:
            print(" ")
            print("--- FIND PASSWORD ---")
            service_name = prompt_non_empty("Enter service name: ")
            status = find_password(session_key, service_name)
            if status["status"] == "success":
                print(f"Password: {status['data']}")
            elif status["status"] == "empty":
                print("No passwords stored yet.")
            elif status["status"] == "not_found":
                print("Password not found")
            elif status["status"] == "file_error":
                print("File not found. Cannot find password.")

        elif choice == 4:
            print(" ")
            print("--- DELETE PASSWORD ---")
            service_name = prompt_non_empty("Enter service name: ")
            
            preview = find_password(session_key, service_name)
            if preview["status"] == "success":
                print(f"Password exists for '{service_name}': {preview['data']}")
                confirm = input("Delete it? (yes/no): ")
                if confirm.lower() != "yes":
                    print("Deletion cancelled.")
                    continue

            status = delete_password(service_name)
            if status["status"] == "deleted":
                print("Password deleted successfully.")
            elif status["status"] == "not_found":
                print("Service not found.")
            elif status["status"] == "empty":
                print("No passwords stored yet.")
            elif status["status"] == "file_error":
                print("File not found or inaccessible")

        elif choice == 5:
            print("Exiting Password Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main()