![CyberPi](https://github.com/user-attachments/assets/7dd8b9cd-400b-4ee2-9581-1dae225d4704)

> Assistive Python programming for CyberPi projects.
#

[CyberPI Hacker](https://chatgpt.com/g/g-6742d1d82d748191a0b2ab9d78538231-cyberpi-hacker) is designed to assist users in programming and utilizing the CyberPi, a versatile microcontroller widely used in STEM education and creative projects. It provides step-by-step guidance, troubleshooting, and clear explanations to help users achieve their goals, whether they're controlling hardware, creating custom functions, or exploring CyberPi's many features. By prioritizing beginner-friendly language and practical examples, it ensures that even those new to programming can effectively engage with CyberPi and the Python programming language.

CyberPi Hacker emphasizes clarity, accessibility, and compatibility with standard libraries and frameworks, enabling users to easily translate their learning into broader programming contexts. It offers conceptual overviews when needed, explaining principles like microcontroller inputs/outputs, sensors, and software logic in simple terms. At the same time, it can delve into more advanced techniques and technical jargon for experienced developers, making it a valuable resource for a wide range of users.

This GPT also excels at personalizing its advice. Through a step-by-step approach and multiple-choice options, it guides users to pinpoint their goals and troubleshoot problems effectively. By focusing on readability and practical implementation, CyberPi Hacker empowers users to unlock CyberPi’s full potential, creating interactive, innovative projects while deepening their understanding of both programming and hardware.

```
Hack the CyberPi with Python.
Explain how to connect CyberPi to external devices.
Print modules and directories.
What are some beginner projects for CyberPi in Python?
Develop a retro cellphone menu.
```

#
### mlink

![makeblock](https://github.com/user-attachments/assets/2ae3f998-c5e0-4ad9-87cd-6fe8f1c6bddd)

mlink is a utility tool used to facilitate communication between a host computer and microcontrollers, such as CyberPi or other devices running MicroPython or similar embedded systems. It allows users to interact with the device's file system, execute Python commands remotely, and manage files, making it an essential tool for developers working with microcontroller-based projects. The backend of mlink typically relies on serial communication over USB (e.g., through COM ports), enabling users to list directories, upload or download files, and run Python scripts directly on the device. This makes it particularly useful for educational robotics platforms like Makeblock, where users can interact with their projects through a command-line interface, enhancing the learning and development process.

The connection between mlink and Makeblock is rooted in their commitment to providing accessible, programmable, and interactive tools for education and robotics. [Makeblock](https://python.mblock.cc/), a prominent Chinese robotics company, uses platforms like CyberPi, which is often paired with tools like mlink, to allow students and hobbyists to program robots and IoT devices. These tools bridge the gap between hardware and software by providing an easy-to-use interface for coding and controlling devices, fostering innovation in STEM education. Additionally, mlink’s backend, built to work seamlessly with these devices, ensures that communication between the user’s computer and the embedded device is efficient and reliable, enabling a smooth user experience for both beginners and advanced users.

#
### Sourceduty Hack Checklist

![display methods](https://github.com/user-attachments/assets/ebb39fa5-c7c2-4c25-854d-b64c3a21d091)

[X] Hack the Cyberpi
<br>
[X] Develop something new for CyberyPi
<br>
[ ] Hack the Cyberpi OS

#
### Python Hacking

![Hacked CyberPi](https://github.com/user-attachments/assets/82955704-1e9d-4924-98d6-d54e1b8df60d)

Hacking the CyberPi without mLink involves leveraging its MicroPython base for direct interaction and programming. The CyberPi supports serial communication, allowing you to bypass mLink using tools like terminal emulators (e.g., PuTTY or screen) and MicroPython utilities such as ampy. Start by connecting the CyberPi via USB and identifying its serial port (e.g., /dev/ttyUSB0 on Linux/macOS or COM ports on Windows). Use a terminal to access the MicroPython REPL, where you can type commands directly to control the device. For example, commands like import cyberpi and cyberpi.led.on('blue') allow you to execute actions in real time. This method provides a hands-on way to program and debug the CyberPi directly, bypassing the need for mLink's graphical interface.

To upload scripts, save your Python code as main.py and use tools like ampy to transfer it to the CyberPi. For instance, the command ampy --port /dev/ttyUSB0 put main.py uploads your script, which will run automatically after the CyberPi reboots. You can also automate commands using Python libraries like pyserial for real-time control, enabling advanced scripting and interaction. This approach gives you flexibility and deeper control over the CyberPi while avoiding reliance on proprietary tools. However, ensure you back up existing scripts and avoid overwriting critical system files to prevent unintended issues. If needed, you can restore default settings via hardware reset or mBlock.

```
help()
```

#
### Classes

Here’s a reliable approach to list the available classes, methods, and attributes from the cyberpi library:

```
import cyberpi

# Inspect the high-level attributes of the cyberpi library
print("High-level members in the cyberpi library:")
print(dir(cyberpi))

print("\nDetailed inspection of each member:")
for member_name in dir(cyberpi):
    print(f"\n--- Inspecting {member_name} ---")
    try:
        member = getattr(cyberpi, member_name)
        print(f"Type: {type(member)}")
        if callable(member):
            print("It is callable (function or method).")
        else:
            print("It is not callable.")
        
        # If it's a class or module, print its contents
        if isinstance(member, type) or isinstance(member, object):
            print("Attributes/Methods:")
            print(dir(member))
    except Exception as e:
        print(f"Could not inspect {member_name}: {e}")
```

#
### Python Built-In

![Hacking](https://github.com/user-attachments/assets/237179b4-92b9-4493-bfde-f2c801225c43)

The files listed, such as boot.py, mainX.py, factoryX.py, and _config.py, represent Python scripts likely used in the CyberPi's runtime environment. These can be modified to tailor the behavior of the device, add custom functionality, or optimize existing processes. To edit these files, you can use a MicroPython-compatible IDE like Thonny, or connect the CyberPi to a computer via USB and access the file system. Through such tools, you can open the files, inspect their contents, and make changes directly in Python. For instance, altering boot.py allows customization of the startup routine, such as initializing hardware components, connecting to Wi-Fi, or running a specific main program.

Before modifying any of these files, it’s crucial to create backups of the original versions to prevent losing the factory configurations or critical functionality. Customizing mainX.py files provides flexibility for different applications, such as running custom scripts for experiments or classroom demonstrations. Similarly, editing factoryX.py might involve tweaking predefined configurations or example programs that showcase specific CyberPi features. The _config.py file often houses important settings, such as hardware calibration values or software parameters. When editing these files, it's essential to follow best practices like commenting on changes, testing modifications incrementally, and ensuring compatibility with the overall system to maintain device stability.

The files listed, such as boot.py, mainX.py, factoryX.py, and _config.py, represent Python scripts likely used in the CyberPi's runtime environment. These can be modified to tailor the behavior of the device, add custom functionality, or optimize existing processes. To edit these files, you can use a MicroPython-compatible IDE like Thonny, or connect the CyberPi to a computer via USB and access the file system. Through such tools, you can open the files, inspect their contents, and make changes directly in Python. For instance, altering boot.py allows customization of the startup routine, such as initializing hardware components, connecting to Wi-Fi, or running a specific main program.

Before modifying any of these files, it’s crucial to create backups of the original versions to prevent losing the factory configurations or critical functionality. Customizing mainX.py files provides flexibility for different applications, such as running custom scripts for experiments or classroom demonstrations. Similarly, editing factoryX.py might involve tweaking predefined configurations or example programs that showcase specific CyberPi features. The _config.py file often houses important settings, such as hardware calibration values or software parameters. When editing these files, it's essential to follow best practices like commenting on changes, testing modifications incrementally, and ensuring compatibility with the overall system to maintain device stability.

#
### Pinout

![Bond](https://github.com/user-attachments/assets/18423212-cccf-4d76-94b4-ce843341d884)

| Pin Name | GPIO Number | Mode       | Description                |
|----------|-------------|------------|----------------------------|
| M1       | GPIO12      | Output     | Motor control/output pin   |
| M2       | GPIO13      | Output     | Motor control/output pin   |
| S1       | GPIO14      | Input      | Sensor input with pull-up  |
| S2       | GPIO15      | Input      | Sensor input with pull-up  |

The table above provides a clear overview of the pin configuration for a CyberPi or ESP32-based setup, detailing the pin names, their respective GPIO numbers, operational modes, and primary functions. Pins M1 and M2 are configured as output pins, commonly used for motor control or other output-based functionalities. Pins S1 and S2, on the other hand, are configured as input pins with pull-up resistors, making them ideal for reading sensor data or detecting external signals. This structured representation simplifies the understanding and utilization of the hardware, especially when integrating various peripherals or debugging pin-related issues.

#
### MicroPython on the ESP32

![Makeblock Product](https://github.com/user-attachments/assets/a995071c-fd19-45bf-b133-03309571e808)

MicroPython on the ESP32 is a powerful tool that brings the simplicity of Python to the hardware programming world, enabling users to interact with GPIO pins, sensors, and actuators through an easy-to-learn scripting language. The ESP32, being a versatile and cost-effective microcontroller with built-in Wi-Fi and Bluetooth, is ideal for IoT projects. MicroPython's lightweight nature makes it suitable for constrained environments, and its extensive library support simplifies tasks like networking, data processing, and hardware control. Developers can easily prototype and iterate their designs, making it a popular choice for both educational purposes and professional embedded system applications. This combination of user-friendliness and capability has driven the widespread adoption of MicroPython on the ESP32 platform.

#

> Alex: "*I like the CyberPi as an easy preassembled Python programming device.*"

#
### Related Links

[ChatGPT](https://github.com/sourceduty/ChatGPT)
<br>
[Raspberry Pi](https://github.com/sourceduty/Raspberry_Pi)
<br>
[Flipper Zero Simulator](https://github.com/sourceduty/Flipper_Zero_Simulator)
<br>
[IoT Hacker](https://github.com/sourceduty/IoT_Hacker)
<br>
[James Bond Gadgets](https://github.com/sourceduty/James_Bond_Gadgets)

***
Copyright (C) 2024, Sourceduty - All Rights Reserved.
