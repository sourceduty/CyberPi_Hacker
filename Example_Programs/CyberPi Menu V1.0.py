# CyberyPi Menu V1.0
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import cyberpi
import time

# Clear the screen
cyberpi.display.clear()

# Define the menu items and their examples
menu_items = [
    "Message 1",
    "Message 2",
    "Message 3",
    "Identity",
    "About"
]

menu_examples = {
    "Message 1": ["Example message content text."],
    "Message 2": ["Example message content text."],
    "Message 3": ["Example message content text."],
    "Identity": ["1234567890'"],
    "License": ["Copyright (C) 2024, Sourceduty - All Rights Reserved."],
    "About": ["CyberyPi Menu V1.0"],
}

# Initial index
current_index = 0
in_submenu = False  # Flag to check if user is in a submenu or not

# Function to display the current menu item
def show_current_item(index):
    """
    Display the currently selected menu item.
    """
    cyberpi.display.clear()
    cyberpi.display.show_label(f"> {menu_items[index]}", size=8, x=5, y=10)

# Function to display the full message
def show_full_message(index):
    """
    Display the entire message content in full screen.
    """
    selected_item = menu_items[index]
    message_lines = menu_examples.get(selected_item, ["No example available."])

    # Display the full message on the screen
    full_message = "\n".join(message_lines)
    cyberpi.display.clear()
    cyberpi.display.show_label(full_message, size=8, x=5, y=10)

# Function to display examples or details for a menu item
def show_example(index):
    """
    Show an example or detailed message for the selected menu item.
    """
    selected_item = menu_items[index]
    
    # Show the full message if it's a message item
    if selected_item.startswith("Message"):
        show_full_message(index)
    else:
        example_text = menu_examples.get(selected_item, "No example available.")
        cyberpi.display.show_label(example_text, size=8, x=5, y=10)

# Initial menu display
show_current_item(current_index)

# Infinite loop to handle navigation and selection
while True:
    # Navigate up
    if cyberpi.controller.is_press("up") and not in_submenu:
        current_index -= 1
        if current_index < 0:  # Wrap around to the last item
            current_index = len(menu_items) - 1
        show_current_item(current_index)
        time.sleep(0.3)  # Debounce

    # Navigate down
    if cyberpi.controller.is_press("down") and not in_submenu:
        current_index += 1
        if current_index >= len(menu_items):  # Wrap around to the first item
            current_index = 0
        show_current_item(current_index)
        time.sleep(0.3)  # Debounce

    # Enter the selected menu with the A button (Select)
    if cyberpi.controller.is_press("a") and not in_submenu:
        # Show the example for the selected menu
        show_example(current_index)
        in_submenu = True  # Mark as being in a submenu
        time.sleep(0.3)  # Debounce to prevent multiple presses

    # Return to the main menu with the B button
    if cyberpi.controller.is_press("b") and in_submenu:
        in_submenu = False  # Mark as exiting the submenu
        show_current_item(current_index)
        time.sleep(0.3)  # Debounce to prevent multiple presses
