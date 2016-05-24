#!/bin/sh
echo "**This script must be run under root or the installation will not run successfully!"
echo "**This program relies on Python and requests lib to run. Make sure you install them correctly."
echo "**The Python directory is set as \"/usr/bin/env python\" by default."
echo "**If it does not matches your Python path,you might need to edit the path yourself before installation."

cp ./drcom.py /usr/bin/drcom
mkdir -p ~/.drcom/
chmod 777 ~/.drcom/

echo "**Installation finish!"
