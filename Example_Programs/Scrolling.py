# Cyberpi Scrolling Text
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import cyberpi
import time

# Clear the screen
cyberpi.display.clear()

# Define the long paragraph text
text = [
    "Hello, CyberPi! This is a demonstration of scrolling text.",
    "We can display longer messages by breaking them into chunks.",
    "Use the joystick to navigate through the text.",
    "CyberPi is a versatile tool for learning and creativity.",
    "Scrolling text makes it easier to read long messages.",
    "Enjoy experimenting with CyberPi and Python!"
]

# Initialize variables for scrolling
current_index = 0  # Start at the first chunk of text

# Function to display the current text chunk
def show_text(index):
    cyberpi.display.clear()  # Clear the screen
    if 0 <= index < len(text):  # Check if index is within bounds
        cyberpi.display.show_label(text[index], size=8)  # Correct usage without x and y

# Initial display
show_text(current_index)

# Infinite loop to handle joystick scrolling
while True:
    # Check for joystick up input
    if cyberpi.controller.is_press("up"):
        if current_index > 0:
            current_index -= 1
            show_text(current_index)
            time.sleep(0.3)  # Prevent rapid scrolling

    # Check for joystick down input
    if cyberpi.controller.is_press("down"):
        if current_index < len(text) - 1:
            current_index += 1
            show_text(current_index)
            time.sleep(0.3)  # Prevent rapid scrolling
