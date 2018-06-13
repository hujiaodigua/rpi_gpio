#!/usr/bin/env python3
# -*- coding=utf-8 -*-

'''
这个脚本控制gdb以及获得返回值
'''

import socket
import os
import sys
import struct
import threading
import time
import tty, termios


def socket_service():
    i = 0

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('192.168.1.111',8888))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('waiting connection...')

    conn, addr = s.accept()
    print('Accept new connection from {0}'.format(addr))
    #conn.recv(4096)
    #print('\r\nw:up, a:left, d:right, s:down, q:stop\r\nc:cut connect')
    while True:
        dht11_tempcture = conn.recv(4096)
        print(dht11_tempcture)
        #pass


if __name__ == '__main__':
    print('')
    socket_service()

