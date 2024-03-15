# In your click.py

from pynput.mouse import Button, Controller
import time

# Initialize the mouse controller
mouse = Controller()
click_count = 0  # Keep track of the number of clicks


def single_click():
    global click_count  # Use the global variable to track clicks across function calls
    click_count += 1  # Increment the click counter

    # Perform a regular left click
    mouse.click(Button.left, 1)
    time.sleep(1)
    # Every 60th click, perform additional actions
    if click_count % 600 == 0:
        # Scroll up (or perform other actions)
        mouse.scroll(0, 1)
        # Hold the right button for 2 seconds
        mouse.press(Button.right)
        time.sleep(2)  # Adjust the sleep time as needed
        mouse.release(Button.right)
        # Scroll down (or perform other actions)
        mouse.scroll(0, -1)

    # Add any other conditional actions here
