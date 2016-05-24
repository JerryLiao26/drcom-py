# drcom-py
This is a Drcom Web Authentication login program written in Python. So generally you should download and install *[Python](https://www.python.org/downloads/)* and *[requests(Python package)](https://github.com/kennethreitz/requests)* first. Note that Embedded version does not need *requests*.

## Version
- **0.1aplha**
This program can only be guaranteed to run among Shenzhen University students who use 'SZU_WLAN' or campus cable network. There are several simple settings can be configured and more will be added to make the program flexible.
- **0.1aplha-em** Embedded version uses *urllib(Python3)* or *urllib,urllib2(Python2)* instead of *requests* to send post data. It also removes some extended function from non-em version.

## Installation Guide
### Embedded
Despite the directory difference('Embedded' but not 'Linux'), refer to Linux method.

### Linux
Go directly to the 'Linux' directory and execute:
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
To uninstall, go to 'Linux' directory and run:
```
sudo ./uninstall.sh
```

### Mac
Not available currently for OS X 10.11 and above, for other versions, refer to Linux method

### Windows
Not available currently

## Known Issues
### Python path incorrect
Manually change the path in drcom.py before you install it.

### Run under Mac OS
Apple has introduced [new security policy](https://en.wikipedia.org/wiki/System_Integrity_Protection) since OS X El Capitan which forbid even root users to write /usr/bin. You might turn it off to use drcom-py but it's not officially recommended.

### Run under Windows OS
You might need to Google yourself to make it run in command line in Windows before official release :-(
