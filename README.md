# drcom-py
This is a Drcom Web Authentication login program written in Python3. So generally you should download and install *[Python3](https://www.python.org/downloads/)* and *[requests(Python package)](https://github.com/kennethreitz/requests)* first.

## Version *0.1alpha*
This program can only be guaranteed to run among Shenzhen University students who use 'SZU_WLAN' or campus cable network. There are several simple settings can be configured and more will be added to make the program flexible.

## Installation Guide
### Linux
Go directly to the Linux directory and execute:
```
sudo ./install.sh
```
After that, you shall run drcom-py in terminal through `drcom` command. Before you start,remember to check the help text:
```
drcom --help
```
or simply:
```
drcom -h
```
To uninstall, go to Linux directory and run:
```
sudo ./uninstall.sh
```

### Mac
Not available currently for OS X 10.11 and above

### Windows
Not available currently

## Issues
### Python3 path incorrect
Manually change the path in drcom.py before you install it.

### Run under Windows OS
You might need to Google yourself to make it run in command line in Windows before official release :-(
