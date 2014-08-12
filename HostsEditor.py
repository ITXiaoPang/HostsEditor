#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ITXiaoPang'

import platform
import os

if __name__ == '__main__':
    #Initial global_variable
    global_platform = platform.system()
    if global_platform == 'Windows':
        global_hosts_path = 'C:\\Windows\\system32\\drivers\\etc'
        global_editor = 'notepad.exe'
    else:
        global_hosts_path = '/etc'
        global_editor = 'vi'
    global_hosts_file = global_hosts_path + os.sep + 'hosts'
    #If can not find the hosts file
    while os.path.isfile(global_hosts_file) is False:
        print('Can not find hosts in ' + global_hosts_path)
        global_hosts_path = raw_input('Please enter the hosts file path:' + os.linesep)
        global_hosts_file = global_hosts_path + os.sep + 'hosts'
    #Show OS Info
    print('Operating System:' + global_platform)
    print('Hosts File Path:' + global_hosts_file)

    #Open Editor
    os.system(global_editor + ' ' + global_hosts_file)