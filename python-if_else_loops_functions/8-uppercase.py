#!/usr/bin/python3

def uppercase(str):
    result = ""
    for c in str:
        # If lowercase letter
        if 97 <= ord(c) <= 122:
            # Convert to uppercase by subtracting 32
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
