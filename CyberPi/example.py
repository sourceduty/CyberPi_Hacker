import cyberpi

# Clear the screen before showing new content
cyberpi.display.clear()

# Set text color to blue
cyberpi.display.set_brush(r=0, g=0, b=255)

# Display "Welcome to CyberPi!" in size 16 at position (0, 0)
cyberpi.display.show_label("Welcome to CyberPi!", size=16, x=0, y=0)
