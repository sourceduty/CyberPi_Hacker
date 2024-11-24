import cyberpi

# Function to display centered text block
def display_centered_text_block(text_block):
    # Clear the display
    cyberpi.display.clear()

    # Simplified grid-based centering
    x = 3  # Centered horizontally (adjust based on your screen size)
    y = 2  # Centered vertically (adjust based on your needs)

    # Display the full text block
    cyberpi.display.label(text_block, x, y)

# Example usage with a multi-line text block
text_block = (
    "#############"
    "#############"
    "#############"
    "#############"
    "#############"
    "#############"
    "#############"
    "#############"
    "########"
)

display_centered_text_block(text_block)
