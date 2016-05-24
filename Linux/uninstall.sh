#!/bin/sh
echo "**This script must be run under root or the uninstallation will not run successfully!"
echo "**The uninstallation will only delete files created by default settings.If you have change the settings,you will need to delete it MANUALLY."

rm -f /usr/bin/drcom

read -p "Delete user config file?[Y/n]:" ANSWER
if [ ${ANSWER} = "Y" ] || [ ${ANSWER} = "y" ]
then
  rm -rf ~/.drcom
  echo "**Uninstallation finish!Thanks for using!"
  exit 0

else
  echo "**Uninstallation finish!You can delete user config file by reruning this script!"
  exit 0

fi
