#! python3
"""Project: phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard."""

import pyperclip
import re

# Define the phone number regex.
phoneRegex = re.compile(r'''(
    (\+44 | 0)  # country code or starting zero
    (\s|-|\.)?  # separator
    (\d{4})     # first 4 digits
    (\s|-|\.)?  # separator
    (\d{6})     # last 6 digits
)''', re.VERBOSE)


# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username - recall special characters are not escaped in a char set
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something 
)''', re.VERBOSE)


# TODO: Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
# There is one tuple for each match, and each tuple contains strings for each group in the regex
for groups in phoneRegex.findall(text):
    # Standardise phone format
    phoneNum = ' '.join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    # Add full email address unaltered
    matches.append(groups[0])

# TODO: Copy results to clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("No phone numbers or email addresses found.")

