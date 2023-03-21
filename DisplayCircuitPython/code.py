"""
Launchpad OLED Addition
Copyright (c) 2023 Simon Peter <probono@puredarwin.org>

This code runs on the Raspberry Pi Pico with CircuitPython.

It has been tested on the Raspberry Pi Pico with Adafruit CircuitPython 8.0.4.

cd /tmp ; wget https://downloads.circuitpython.org/bin/raspberry_pi_pico/en_US/adafruit-circuitpython-raspberry_pi_pico-en_US-8.0.4.uf2
cp /tmp/adafruit-circuitpython-raspberry_pi_pico-en_US-8.0.4.uf2 /media/RPI-RP2

cd /tmp ; wget https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20230319/adafruit-circuitpython-bundle-8.x-mpy-20230319.zip
# Unzip
cp /tmp/user/_tmp_adafruit-circuitpython-bundle-8.x-mpy-20230319.zip/adafruit-circuitpython-bundle-8.x-mpy-20230319/lib/adafruit_ssd1306.mpy /media/msdosfs/lib
cp -r /tmp/user/_tmp_adafruit-circuitpython-bundle-8.x-mpy-20230319.zip/adafruit-circuitpython-bundle-8.x-mpy-20230319/lib/adafruit_displayio_* /media/msdosfs/lib
"""

import usb_cdc
import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

WIDTH = 128
HEIGHT = 64

# Initialize the display
i2c = busio.I2C(board.GP3, board.GP2, frequency=400000)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
display = adafruit_displayio_ssd1306.SSD1306(
    display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group()
display.show(splash)

# Create the color bitmap and palette
color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

# Create the background sprite
bg_sprite = displayio.TileGrid(
    color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Create the inner rectangle sprite
BORDER = 2
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
splash.append(inner_sprite)

# Secondary ttyUSB port (first is Python REPL)
# This needs to be set up in boot.py
serial = usb_cdc.data

in_data = bytearray()

text_areas = []
text_area_index = 0

while True:
    # Check for incoming data
    if serial.in_waiting > 0:
        byte = serial.read(1)
        if byte == b'\r':
            print(in_data.decode("utf-8"))
            out_data = in_data
            in_data = bytearray()

            # Clear the background sprite
            for i in range(len(bg_sprite)):
                bg_sprite[i] = 0

            # Remove existing text areas
            for text_area in text_areas:
                splash.remove(text_area)
            text_areas = []
            text_area_index = 0

            # Draw the text
            text = out_data.decode("utf-8").strip()
            # Split text into up to 6 lines with 20 characters each
            lines = [text[i:i+20] for i in range(0, len(text), 20)]
            y = 5
            for line in lines:
                if text_area_index < len(text_areas):
                    # Reuse an existing text area
                    text_area = text_areas[text_area_index]
                else:
                    # Create a new text area
                    text_area = label.Label(
                        terminalio.FONT, text=line, color=0xFFFFFF, x=0, y=y
                    )
                    text_areas.append(text_area)
                splash.append(text_area)
                text_area.text = line
                text_area_index += 1
                y += 10
        else:
            in_data += byte
