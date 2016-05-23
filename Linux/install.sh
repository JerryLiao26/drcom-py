#!/bin/sh
echo "**This script must be run under root or the installation will not run successfully!"
echo "**This program relys on Python3 and requests lib to run.Make sure you install them correctly."
echo "**The Python3 directory is set as \"/usr/bin/python3\" by default."
echo "**If it does not matches your Python3 path,you should edit the path yourself before installation."

cp ./drcom.py /usr/bin/drcom
mkdir -p ~/.drcom/

echo "**Installation finish!"
