# coding=utf8

import sys
from cx_Freeze import setup, Executable

setup(
    name = "test",
    version = "2.7",
    description = u"妈妈再也不担心今天吃哪个食堂",
    executables = [Executable("restaurant.py", base = "Win32GUI")])