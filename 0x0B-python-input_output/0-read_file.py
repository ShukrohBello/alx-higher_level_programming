#!/usr/bin/python3
"""A function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Reads from filenaem and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        read_text = f.read()
        printf(read_text, end="")
