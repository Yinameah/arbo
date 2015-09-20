#!/usr/bin/env python3
"""
Main file for app, a mind mapping tool

Simply import Arbo (application) class and run Qt main loop

author : Aurelien Cibrario <aurelien.cibrario@gmail.com>

"""

import sys
from src.app import Arbo

if __name__ == '__main__':
    app = Arbo(sys.argv)
    sys.exit(app.run())