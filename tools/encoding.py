#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO
danda = font['u0C66']
danda.name = 'zero.telu'

# Save UFO
font.changed()
font.save()
font.close()
