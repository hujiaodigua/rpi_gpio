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
        s.bind(('192.168.1.111',7777))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('waiting connection...')

    conn, addr = s.accept()
    print('Accept new connection from {0}'.format(addr))
    #conn.recv(4096)
    print('\r\nw:up, a:left, d:right, s:down, q:stop\r\nc:cut connect')
    while True:
        #input_data = input('please input:')
        #conn.send(input_data.encode('utf-8'))
        #conn.send(b'w')
        #time.sleep(2)
        #conn.send(b'a')
        #time.sleep(2)
        #conn.send(b'cutoff')

        #监视按键，获取键值放在ch中
        fd=sys.stdin.fileno()
        old_settings=termios.tcgetattr(fd)
        #old_settings[3]= old_settings[3] & ~termios.ICANON & ~termios.ECHO
        try:
            tty.setraw(fd)
            ch=sys.stdin.read(1)
	    #ch_next=sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        if ch=='w':
           # i=i+1
           # if i == 1:
                conn.send(b'w')
                print('up')
        elif ch=='a':
            conn.send(b'a')
            print('left')
        elif ch=='d':
            conn.send(b'd')
            print("right!")
        elif ch=='s':
            conn.send(b's')
            print("down")
        elif ch=='q':
            conn.send(b'q')
            print("stop")
        elif ch=='c':
            print("cut connect")
            conn.send(b'cutoff')
            time.sleep(1)
            sys.exit(0)

if __name__ == '__main__':
    print('')
    socket_service()

