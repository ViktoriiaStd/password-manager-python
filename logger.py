from datetime import datetime
LOG_FILE = "audit.log"

def log_action(user, action, details=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if details:
        log_line = f"[{timestamp}] USER={user} ACTION={action} DETAILS={details}\n"
    else:
        log_line = f"[{timestamp}] USER={user} ACTION={action}\n"

    with open(LOG_FILE, "a") as f:
        f.write(log_line)