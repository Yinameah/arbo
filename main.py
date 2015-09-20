#!/usr/bin/env python3
"""
Main file for app, a mind mapping tool

Importe simplement la classe Arbo et lance le loop Qt

author : Aurelien Cibrario <aurelien.cibrario@gmail.com>

"""

import sys
from src.app import Arbo

if __name__ == '__main__':
    app = Arbo(sys.argv)
    sys.exit(app.run())