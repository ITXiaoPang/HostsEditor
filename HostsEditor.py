#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ITXiaoPang'

import platform

if __name__ == '__main__':
    global_platform = platform.system();
    print('Current OS:' + global_platform);
    if global_platform == 'Windows':
        global_hosts_path = 'C:\\windows\\system32\\drivers\\etc\\';
    else:
        global_hosts_path = '/etc/';
    print('Current Hosts File Path:' + global_hosts_path + 'hosts');