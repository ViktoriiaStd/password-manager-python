# Password Manager (Python)

A simple console-based password manager written in Python.  
This project demonstrates basic security principles such as password validation, encryption, logging, and modular design.

---

## Features

- Add, view, find, and delete stored passwords
- Password validation (length, uppercase, lowercase, digit, special character)
- Encrypted password storage
- Masked password display
- Logging of user actions
- Input validation to prevent empty values
- Unit tests for password validation

---

## Tech Stack

- Python 3
- Standard Library (`os`, `sys`, `logging`)
- `cryptography` (Fernet) for encryption
- `pytest` for unit testing

---

## Project Structure

password-manager-python/
│
├── main.py # Application entry point (menu logic)
├── auth.py # Authentication logic
├── storage.py # Password storage operations
├── crypto_utils.py # Encryption / decryption utilities
├── validation.py # Input & password validation
├── logger.py # Logging configuration
├── tests/
│ └── test_validation.py
├── .gitignore
└── README.md


---

## How to Run

1. Clone the repository:
```
git clone https://github.com/ViktoriiaStd/password-manager-python.git
cd password-manager-python
```
2. Run the application:
```
python main.py
```

---

## Running Tests

1. Make sure pytest is installed
```
pip install pytest
```
2. Run tests:
```
pytest
```

---

## Security Notes
- Passwords are never stored in plain text
- Password strength is validated before saving
- Sensitive data is masked when displayed
- Project is for educational purposes and not intended for production use
- Encryption keys are generated per session and not hardcoded

---

## Purpose
- This project was created as a learning exercise to practice:
    * Python fundamentals
    * Secure coding basics
    * Modular project structure
    * Unit testing
    * Working with Git and GitHub

---

## Future Improvements
- Implement a master password with secure hashing (PBKDF2 / bcrypt)
- Role-based access and multi-user support
- Store encrypted passwords in a database instead of local files
- Password strength meter and reuse detection
- Automatic password expiration and rotation
- Secure clipboard copy with timeout
- Improved logging and audit trail
- More unit and integration tests
- GUI or web-based interface

---
 
## Author
Viktoriia Studeniak
Junior Network & Cybersecurity Enthusiast
