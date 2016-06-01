#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys, json, requests

# Get python major version
py_version_index = str(sys.version_info).index('major')
py_version = str(sys.version_info)[(py_version_index + 6) : (py_version_index + 7)]

if py_version == "2": # Python 2.x
    from Tkinter import *
    import tkMessageBox as messagebox
else: # Python 3.x and above
    from tkinter import *
    import tkinter.messagebox as messagebox

# Global params
version = "0.1release-gui-20160526"
param_num = len(sys.argv)
self_name = sys.argv[0]
file_path = os.path.expanduser("~") + "/.drcom/drcom.config" # Create config file under ~/.drcom/
auth_url = "http://192.168.254.220/a70.htm"
api_site = "http://api.jerryliao.cn/" # Default api url
api_type = "php" # Requested api file type
stu_no = "jf"
pwd = "jf"

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.stuLabel = Label(self, text='Student no')
        self.stuLabel.pack()
        self.stuInput = Entry(self) # Stu_no input
        self.stuInput.pack()

        self.pwdLabel = Label(self, text='Password')
        self.pwdLabel.pack()
        self.pwdInput = Entry(self) # Password input
        self.pwdInput.pack()
        self.pwdInput['show'] = '*'

        self.loginButton = Button(self, text='Login', command=self.login)
        self.loginButton.pack()
        self.quitButton = Button(self, text='Status', command=self.status)
        self.quitButton.pack()

        self.versionLabel = Label(self, text=version)
        self.versionLabel.pack()

    # Load settings in drcom.config
    def load_config():
        try:
            global stu_no, pwd, auth_url
            with open(file_path, 'r') as in_config:
                config = json.load(in_config)
                stu_no = config["stu_no"]
                pwd = config["pwd"]
                auth_url = config["auth_url"]
                api_site = config["api_site"]
                api_type = config["api_type"]
        except IOError:
            set_config()

    # Write settings in drcom.config
    def set_config():
        config = {
            "stu_no" : stu_no,
            "pwd" : pwd,
            "auth_url" : auth_url,
            "flag" : "develop",
            "api_site" : api_site,
            "api_type" : api_type
        }
        with open(file_path, 'w') as out_config:
            json.dump(config, out_config)

    def login(self):
        if self.stuInput.get() == "":
            messagebox.showinfo('Attention', 'Student no can\'t be null!')
        if self.pwdInput.get() == "":
            messagebox.showinfo('Attention', 'Password can\'t be null!')

        if self.stuInput.get() != "" and self.pwdInput.get() != "":
            self.load_config

            global stu_no, pwd
            stu_no = self.stuInput.get()
            pwd = self.pwdInput.get()

            self.set_config

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

            r = requests.post(auth_url_login, data=login_data)
            try:
                message_index = r.text.index("msga") # Param containing error message
                message_start_index = r.text.index("'", message_index)
                message_end_index = r.text.index("'", message_start_index + 1)
                respond = r.text[(message_start_index + 1) : message_end_index]
            except ValueError:
                respond = "login success"
            finally:
                messagebox.showinfo('Server respond', respond)

    def status(self):
        message_string = ""
        user_agent_str = "drcom-py/" + version
        api_url_ua = api_site + "echo_ua." + api_type
        api_url_ip = api_site + "echo_ip." + api_type
        headers = {
            "User-Agent" : user_agent_str
        }

        # Internet connection status
        r = requests.get(url=api_url_ua, headers=headers)
        if r.text == user_agent_str: # Not blocked by Drcom
            message_string += "Internet...connected,"
            r = requests.get(url=api_url_ip)
            message_string += " IP: " + r.text + os.linesep
        else:
            message_string += "Internet...disconnected" + os.linesep

        # Intranet connection status
        try:
            r = requests.get(url=auth_url, timeout=5)
            message_string += "Campus Intranet...connected,"
            intranet_status = 1
            intranet_ip_start_index = r.text.index('v46ip') # Find Intranet IP
            intranet_ip_end_index = r.text.index('\'', intranet_ip_start_index + 7)
            intranet_ip = r.text[(intranet_ip_start_index + 7) : intranet_ip_end_index]
            message_string += " IP: " + intranet_ip
        except Exception:
            message_string += "Campus Intranet...disconnected"

        messagebox.showinfo('Status', message_string)

# Start GUI
app = Application()
app.master.title('drcom-py')
app.master.maxsize(200, 160)
app.master.minsize(200, 160)
app.mainloop()
