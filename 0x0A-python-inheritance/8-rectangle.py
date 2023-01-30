#!/usr/bin/python3
"""placeholder"""
BaseGeometry = _import_('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def _init_(self, width, height):
        self._width = width
        self._height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
