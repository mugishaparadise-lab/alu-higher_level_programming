#!/usr/bin/python3


def uppercase(str):
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:  # if lowercase letter
            result += chr(ord(c) - 32)  # convert to uppercase
        else:
            result += c
    print("{}".format(result))
