#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import socket
import uuid

def get_mac_address():
      node = uuid.getnode()
      mac = uuid.UUID(int = node).hex[-12:]
      return mac

def get_compute_mac():
    # 获取本机电脑名
    myname = socket.getfqdn(socket.gethostname())
    # 获取本机ip
    myaddr = socket.gethostbyname(myname)
    return myaddr
