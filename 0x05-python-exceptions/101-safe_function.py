#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None

# Example functions for testing
def divide(a, b):
    return a / b

def concatenate_strings(str1, str2):
    return str1 + str2
