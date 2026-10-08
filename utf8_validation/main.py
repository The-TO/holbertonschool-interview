#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [250, 145, 145, 145, 145]
print(validUTF8(data))