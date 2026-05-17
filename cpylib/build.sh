#!/usr/bin/env bash

# sudo apt update
# sudo apt install python3-dev

# VSCode:
# CTRL+SHIFT+P > C/C++ Edit Configuration (UI)
# Under Include Path, add 
#   /usr/include/python3.*/**
# (Might have to add without the wildcard, and let VSCode fill wildcard in.)

python3 setup.py build_ext --inplace