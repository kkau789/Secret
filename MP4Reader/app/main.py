#!/usr/bin/env python3
import curses
from src import main_module  # Import the module we just made

if __name__ == "__main__":
    curses.wrapper(main_module.menu)
