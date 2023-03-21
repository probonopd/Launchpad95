#!/usr/bin/env python3

"""
Launchpad OLED Addition
Copyright (c) 2023 Simon Peter <probono@puredarwin.org>

This script runs on the host computer.
It continuously reads the Ableton Live Log file, parses it for
information that should be displayed on the OLED display,
and sends it out via the serial port to the Raspberry Pi Pico
running CircuitPython firmware to which the OLED display is connected.
Having this as a separate script (not run by Ableton Live)
has the following advantages:
* Can be changed and restarted on the fly,
  without having to restart Ableton Live
* Can use Python modules unavailable in the Python
  that comes with Ableton Live
* Works even if Ableton Live is running in WINE
"""

import serial.tools.list_ports
import time
import os
import threading

# Define the path to the log file
log_file_path = "/usr/home/user/.wine/drive_c/users/steamuser/AppData/Roaming/Ableton/Live 11.2.6/Preferences/Log.txt"


class SerialDisplay:

    def __init__(self):
        self.attributes = []
        self.attribute_names = []
        self.message = ""
        self.port = None
        self.timer = None
        for port in serial.tools.list_ports.comports():
            print("Found port: %s" % port.device)
            # Unbuffered serial port
            self.port = serial.Serial(port.device, 115200, timeout=0)

    def print(self, text):
        if self.port is not None:
            text_bytes = text.encode('utf-8')
            self.port.write(text_bytes + b'\r\n')

    def output_message(self):
        self.print(display.message)
        if self.timer is not None and self.timer.is_alive():
            self.timer.cancel()
        self.timer = threading.Timer(3.0, self.output)
        self.timer.start()

    def output(self):
        content = ""
        for i in range(0, len(self.attributes)):
            try:
                content = content + self.attribute_names[i] + \
                    ": " + self.attributes[i] + ", "
            except IndexError:
                pass
        content = content[:-2]  # Remove the last comma and space
        self.print(content)


if __name__ == '__main__':

    display = SerialDisplay()

    if display.port is None:
        print("No serial port available")
        exit(1)

    # Check if at least one serial port is available
    if not display.port:
        print("No serial port available")
        exit(1)

    # Get the initial size of the log file
    last_size = os.path.getsize(log_file_path)

    while True:
        # Check the size of the log file
        size = os.path.getsize(log_file_path)

        # If the size has increased, print the new lines
        if size > last_size:
            with open(log_file_path, 'r') as f:
                # Move the file pointer to the last read position
                f.seek(last_size)

                # Read the new data and split into lines
                new_data = f.read(size - last_size)
                new_lines = new_data.split('\n')

                # Print each new line
                for line in new_lines:
                    if line.strip() == "":
                        continue
                    # print("-> " + line)

                    if "message:" in line:
                        message = line.split("message: ")[1].strip()
                        # print("--> " + message)
                        # display.print(message)
                        display.message = message
                        display.output_message()

                    if "attributes:" in line:
                        attributes = line.split("attributes:")[1].strip()
                        # attributes is a string of the form
                        # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                        # We need to convert it to a list
                        attributes = attributes[1:-1].split(',')
                        attributes = [attribute.replace("'", "").strip()
                                      for attribute in attributes]
                        # Remove empty attributes
                        attributes = [attribute for attribute in attributes
                                      if attribute != ""]
                        display.attributes = attributes
                        # If the timer is not running, print the attributes
                        if display.timer is None or not display.timer.is_alive():
                            display.output()

                    if "attribute_names:" in line:
                        attribute_names = line.split(
                            "attribute_names:")[1].strip()
                        # attributes is a string of the form
                        # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                        # We need to convert it to a list
                        attribute_names = attribute_names[1:-1].split(',')
                        attribute_names = [attribute_name.replace("'", "").strip()
                                           for attribute_name in attribute_names]
                        # Remove empty attributes
                        attribute_names = [attribute_name for attribute_name in attribute_names
                                           if attribute_name != ""]
                        display.attribute_names = attribute_names

                # Update the last size
                last_size = size

        # Wait for a short period of time before checking again
        time.sleep(0.05)
