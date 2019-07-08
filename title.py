"""
Title screen, main menu, etc
"""
from support.helpers import sleep, clear_screen


def splash_screen():
    """
    Displays the game splash screen

    :return:
    """
    clear_screen()
    print("""
             ┌─────────────────────────────────────────────────────────┐
             │                                                         │
             │                                                         │
             │ ┌───────────────────   SysRunner   ───────────────────┐ │
             ├─┘                                                     └─┤
             ├─┐                                                     ┌─┤
             │ └──────────── A Rogue-Lite Text Adventure ────────────┘ │
             │                                                         │
             │                                                         │
             └─────────────────────────────────────────────────────────┘
    """)
    sleep(3)
