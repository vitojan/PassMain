# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:34:32 2023

@author: VitoJan
"""

import pyperclip

text_to_copy = "This is the text you want to copy to the clipboard."
pyperclip.copy(text_to_copy)

clipboard_text = pyperclip.paste()
print("Clipboard contains:", clipboard_text)
