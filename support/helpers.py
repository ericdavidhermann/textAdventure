"""
Helper functions used in various places
"""
import time
import os


def sleep(seconds):
    """
    Alias function for time.sleep(x)

    :param seconds: How long to sleep
    :return: Nothing
    """
    time.sleep(seconds)


def clear_screen():
    """
    Clears the screen

    :return: Nothing
    """
    os.system('cls' if os.name == 'nt' else 'clear')
