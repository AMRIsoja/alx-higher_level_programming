#!/usr/bin/python3
def print_last_digit(number):
    print(f"{-(number % 10) if number < 0 else number % 10}")
    return -(number % 10) if number < 0 else number % 10
