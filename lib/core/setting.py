#!/usr/bin/env python
#encoding: utf-8
#author:zeroyu
#project:https://github.com/zer0yu/ZEROScan

import os
import subprocess

VERSION = '1.0.0'
VERSION_STRING = "ZEROScan"
AUTHOR = 'zeroyu'
PLATFORM = os.name
IS_WIN = subprocess.mswindows

ESSENTIAL_MODULE_METHODS = [
    'audit'
]

UNICODE_ENCODING = "utf-8"

NULL = "NULL"

INVALID_UNICODE_CHAR_FORMAT = r"\x%02x"

BANNER = """\033[01;34m
  _______  \033[01;31m__/\033[01;34m
 /_____  / \033[01;33m/ \033[01;31m__/\033[01;34m
     /  /  \033[01;33m_/\033[01;34m
    /  /    
   /  /____    
  /_______/
    \033[01;37m{\033[01;m Version %s by %s mail:%s \033[01;37m}\033[0m
\n""" % (VERSION, AUTHOR, MAIL)


