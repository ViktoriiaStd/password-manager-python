import re

def validate_password(password):
    """
    Password MUST contain:
    - Minimum 8 characters
    - At least 1 uppercase letter
    - At least 1 lowercase letter
    - At least 1 special character (!@#$%^&*()_+-=[]{};:',.<>/?)
    - At least 1 digit
    """
    errors = []
    if len(password) < 8:
        errors.append("- At least 8 characters")
        
    if not re.search(r"[A-Z]", password):
        errors.append("- At least one uppercase letter")
    if not re.search(r"[a-z]", password):
        errors.append("- At least one lowercase letter")
    if not re.search(r"\d", password):
        errors.append("- At least one digit")
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{}|;:',.<>/?]", password):
        errors.append("- At least one special character (!@#$%^&*():')")
    
    return errors


def prompt_non_empty(prompt_text):
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print("Input cannot be empty. Try again.")