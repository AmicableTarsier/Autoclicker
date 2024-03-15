import tkinter as tk
from click import single_click
from pynput import keyboard
import threading
import time

# Initialize autoclicker_running at the top of the script to ensure it's globally accessible
autoclicker_running = False
autoclicker_thread = None  # Keep track of the autoclicker thread


def autoclicker_task():
    while autoclicker_running:
        single_click()


def start_autoclicker():
    time.sleep(10)
    global autoclicker_running, autoclicker_thread
    if not autoclicker_running:  # Only start if the autoclicker is not already running
        autoclicker_running = True
        # Only create a new thread if the previous one is not running
        if autoclicker_thread is None or not autoclicker_thread.is_alive():
            autoclicker_thread = threading.Thread(target=autoclicker_task, daemon=True)
            autoclicker_thread.start()


def stop_autoclicker():
    global autoclicker_running
    autoclicker_running = False  # This will cause the thread to finish


def on_press(key):
    try:
        if key.char == 'r':  # Checks if 'r' was pressed
            stop_autoclicker()
    except AttributeError:
        pass  # Special keys will throw this error


# Create the main window
window = tk.Tk()
window.title("Minecraft Autoclicker")
window.configure(bg='light blue')

# Main frame
main_frame = tk.Frame(window, bg='light gray', bd=2, relief='groove')
main_frame.pack(padx=10, pady=10, fill='both', expand=True)

# Header label
header = tk.Label(main_frame, text="Minecraft Autoclicker", font=('Arial', 24, 'bold'), bg='light gray')
header.pack(pady=(5, 10))

# Instruction label
instruction = tk.Label(main_frame, text="Have a sword with Mending Enchantment in your first slot\n "
                                        "Have food in your last slot", font=('Arial', 12), bg='light gray')
instruction.pack(pady=(0, 20))

# Start button
start_button = tk.Button(main_frame, text="Start", font=('Arial', 12), bg='green', fg='white',
                         activebackground='light green', padx=10, pady=5,
                         command=start_autoclicker)
start_button.pack()

instruction2 = tk.Label(main_frame, text="Autoclicker will begin 10 seconds after pressing button",
                        font=('Arial', 12), bg='light gray')
instruction2.pack(pady=(0, 20))

escape_key = tk.Label(main_frame, text="Press 'R' to cancel Autoclicker", font="Arial 20 bold", bg='light gray')
escape_key.pack(pady=(0, 20))

# This line starts the listener in a non-blocking way
listener = keyboard.Listener(on_press=on_press)
listener.start()

window.mainloop()

# Ensure the listener is stopped when the mainloop ends
if listener.running:
    listener.stop()
