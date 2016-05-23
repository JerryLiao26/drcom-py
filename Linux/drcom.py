#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os,sys,requests

# Global params
param_num = len(sys.argv)
self_name = sys.argv[0]
file_path = os.path.expanduser("~") + "/.drcom/drcom.config" # Create config file under ~/.drcom/
auth_url = "http://192.168.254.220/a70.htm"
stu_no = "jf"
pwd = "jf"
flag = "develop"

# Load settings in config.ini
def load_config():
    try:
        global stu_no,pwd,auth_url

        config_file = open(file_path, 'r')
        file_stream = config_file.read() # Read the config file
        stu_no_index = file_stream.index("stu_no:") # Get all the config settings' index
        pwd_index = file_stream.index("pwd:")
        auth_url_index = file_stream.index("auth_url:")

        stu_no = file_stream[(stu_no_index + 7) : (pwd_index - 1)] # Set as config.ini
        pwd = file_stream[(pwd_index + 4) : (auth_url_index - 1)]
        auth_url = file_stream[(auth_url_index + 9) : len(file_stream)]

        config_file.close()

    except IOError:
        set_config()

# Write settings in config.ini
def set_config():
    with open(file_path, 'w') as config_file:
        config_file.write('===========\r\nUser Info\r\n===========\r\nstu_no:' + str(stu_no) + '\r\npwd:' + str(pwd) + '\r\nauth_url:' + auth_url)

# Start drcom confirm
def confirm():
    load_config()

    # Currently depends on http://192.168.254.220/a41.js (shorten as "a41.js")
    stu_no_login = stu_no
    pwd_login = pwd
    auth_url_login = auth_url

    login_data = {
        'DDDDD' : stu_no_login,
        'upass' : pwd_login,
        'R1' : '0', # Defined in function cc in a41.js
        'R2' : '', # Defined in function ee in a41.js
        'R6' : '0',
        'para' : '00',
        '0MKKey' : '123456'
    }

    r = requests.post(auth_url_login,data = login_data)

    try:
        message_index = r.text.index("msga") # Param containing error message
        message_start_index = r.text.index("'",message_index)
        message_end_index = r.text.index("'",message_start_index + 1)
        respond = r.text[(message_start_index + 1) : message_end_index]

    except ValueError:
        respond = "login success"

    finally:
        print('Server respond:' + respond)

if param_num == 1: # Use default settings
    confirm()

# elif sys.argv[1] == "--develop" or sys.argv[1] == "-d": # Start develop mode
#     flag = develop
#
# elif sys.argv[1] == "--user" or sys.argv[1] == "-u": # Start user mode
#     flag = user

elif sys.argv[1] == "--show" or sys.argv[1] == "-s": # Show present settings
    load_config()
    if flag == "develop":
        print("stu_no:" + str(stu_no) + "\r\npwd:" + str(pwd) + "\r\nauth_url:" + auth_url)

    else:
        print('Not under develop mode!')
        exit()

elif sys.argv[1] == "--help" or sys.argv[1] == "-h": # List help text
    print('Usage:')
    # print('--dev | -d Start develop mode')
    # print('--user | -u Start user mode')
    print('--show | -s Show present settings (Only under develop mode)')
    print('--help | -h Display this text')
    print('--config | -c Configure settings')
    print('--config [setting_name] | -c [setting_name] Configure specific setting')

elif sys.argv[1] == "--config" or sys.argv[1] == "-c": # Use custom settings,pressing enter will use default
    load_config()

    input_stu_no = input_pwd = input_file_path = input_auth_url = "" # Initialize

    if param_num == 2:
        input_stu_no = input("stu_no:")
        input_pwd = input("pwd:")
        input_auth_url = input("auth_url:")

    elif param_num == 3:
        if sys.argv[2] == "stu_no":
            input_stu_no = input("stu_no")

        elif sys.argv[2] == "pwd":
            input_pwd = input("pwd")

        elif sys.argv[2] == "auth_url":
            input_pwd = input("auth_url")

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
