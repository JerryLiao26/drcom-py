#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,sys,json

# Get python major version
py_version_index = str(sys.version_info).index('major')
py_version = str(sys.version_info)[(py_version_index + 6) : (py_version_index + 7)]

if py_version == "2": # Python2.x
    from urllib2 import Request,urlopen
    from urllib import urlencode
    input = raw_input

else: # Python 3.x and above
    from urllib.request import Request,urlopen
    from urllib.parse import urlencode

# Global params
version = "0.1beta-em-20160525"
param_num = len(sys.argv)
self_name = sys.argv[0]
file_path = os.path.expanduser("~") + "/.drcom/drcom.config" # Create config file under ~/.drcom/
auth_url = "http://192.168.254.220/a70.htm"
stu_no = "jf"
pwd = "jf"

# Load settings in config.ini
def load_config():
    try:
        global stu_no,pwd,auth_url

        with open(file_path, 'r') as in_config:
            config = json.load(in_config)
            stu_no = config["stu_no"]
            pwd = config["pwd"]
            auth_url = config["auth_url"]

    except IOError:
        set_config()

# Write settings in config.ini
def set_config():
    config = {
        "stu_no" : stu_no,
        "pwd" : pwd,
        "auth_url" : auth_url
    }
    with open(file_path, 'w') as out_config:
        json.dump(config,out_config)

# Start drcom confirm
def confirm():
    load_config()

    # Currently depends on http://192.168.254.220/a41.js (shorten as "a41.js")
    stu_no_login = stu_no
    pwd_login = pwd
    auth_url_login = auth_url

    login_data = {
        "DDDDD" : stu_no_login,
        "upass" : pwd_login,
        "R1" : "0", # Defined in function cc in a41.js
        "R2" : "", # Defined in function ee in a41.js
        "R6" : "0",
        "para" : "00",
        "0MKKey" : "123456"
    }

    r = Request(auth_url_login)
    f = urlopen(url = auth_url_login,data = urlencode(login_data).encode('utf-8')) # Encode to be used under Python3
    text = f.read().decode('gbk')
    f.close()

    try:
        message_index = text.index("msga") # Param containing error message
        message_start_index = text.index("'",message_index)
        message_end_index = text.index("'",message_start_index + 1)
        respond = text[(message_start_index + 1) : message_end_index]

    except ValueError:
        respond = "login success"

    finally:
        print('Server respond:' + respond)

if param_num == 1: # Use default settings
    confirm()

elif sys.argv[1] == "--show" or sys.argv[1] == "-s": # Show present settings
    load_config()
    print("stu_no:" + str(stu_no) + os.linesep + "pwd:" + str(pwd) + os.linesep + "auth_url:" + auth_url)

elif sys.argv[1] == "--help" or sys.argv[1] == "-h": # List help text
    print('Usage:')
    print('--show | -s Show present settings')
    print('--help | -h Display this text')
    print('--config | -c Configure settings, enter for default')
    print('--config [setting_name] | -c [setting_name] Configure specific setting, enter for default')
    print('--version | -v Show the version of this program')

elif sys.argv[1] == "--version" or sys.argv[1] == "-v":
    print('drcom-py version : ' + version)
    print('Author: jerryliao')
    print('Email: jerryliao26@gmail.com')

elif sys.argv[1] == "--config" or sys.argv[1] == "-c": # Use custom settings,pressing enter will use default
    load_config()

    input_stu_no = input_pwd = input_file_path = input_auth_url = "" # Initialize

    if param_num == 2:
        input_stu_no = input("stu_no:")
        input_pwd = input("pwd:")
        input_auth_url = input("auth_url:")

    elif param_num == 3:
        if sys.argv[2] == "stu_no":
            input_stu_no = input("stu_no:")

        elif sys.argv[2] == "pwd":
            input_pwd = input("pwd:")

        elif sys.argv[2] == "auth_url":
            input_auth_url = input("auth_url:")

        else:
            print('invalid param ' + sys.argv[2] + '! Please check "--help" or "-h" for usage')
            exit()

    if input_stu_no == "":
        input_stu_no = stu_no

    if input_pwd == "":
        input_pwd = pwd

    if input_auth_url == "":
        input_auth_url = auth_url

    stu_no = input_stu_no
    pwd = input_pwd
    auth_url = input_auth_url

    set_config()

else:
    print('invalid param ' + sys.argv[1] + '! Please check "--help" or "-h" for usage')
    exit()
