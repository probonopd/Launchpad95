"""
Launchpad OLED Addition
Copyright (c) 2023 Simon Peter <probono@puredarwin.org>

This code runs on the Raspberry Pi Pico with CircuitPython.
"""

import usb_cdc

# Enable console and data
usb_cdc.enable(console=True, data=True)
