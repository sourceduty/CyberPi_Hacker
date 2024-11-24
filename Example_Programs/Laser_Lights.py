import cyberpi
import time

def laser_lights():
    """
    A laser light effect featuring flashing red LEDs, dynamic text display, 
    and synchronized sound effects, mimicking a laser show.
    """
    # Define the laser light color (red)
    led_color = (255, 0, 0)
    
    # Loop for the light and sound effect
    for _ in range(15):  # Perform the effect 15 times
        # Turn on the red LEDs
        cyberpi.led.on(led_color[0], led_color[1], led_color[2])
        
        # Display "LASER" with a bright yellow background
        cyberpi.display.set_brush(255, 255, 0)  # Yellow background
        cyberpi.display.clear()
        cyberpi.display.show_label("LASER", 24, "center")
        
        time.sleep(0.2)  # Short pause
        
        # Turn off LEDs and display a cool-down message with a black background
        cyberpi.led.off()
        cyberpi.display.set_brush(0, 0, 0)  # Black background
        cyberpi.display.clear()
        cyberpi.display.show_label("COOLING", 15, "center")
        
        time.sleep(0.2)  # Short pause
        
        # Play the laser sound effect
        cyberpi.audio.play("laser")
    
    # Final cleanup: Turn off LEDs and reset the screen
    cyberpi.led.off()
    cyberpi.display.set_brush(0, 0, 0)  # Reset screen to black
    cyberpi.display.clear()
    print("Laser Light Show Finished!")

# Run the laser light show
laser_lights()
