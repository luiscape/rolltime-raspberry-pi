#!/usr/bin/python
# -*- coding: utf-8 -*-

def GeneratePixels(n):
  '''Generates pixels for the SenseHat.'''

  #
  # Fill colors.
  #
  X = [255, 0, 0]  # Red
  O = [255, 255, 255]  # White

  pixels = [ X for i in range(n) ]
  pixels += [ O for i in range(64 - n) ]

  return pixels
