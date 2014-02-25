#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename: sendmail.py
# 

import os
import subprocess

def winrar(rar_filename, src_dir):
    file_path   = os.path.dirname(__file__)
    abs_path    = os.path.abspath(file_path)
    cmd_path    = abs_path+"\\"+"rar.exe"
    cmd = "%s a -ibck -inul -df -m5 -hp[test] %s %s/*" % (cmd_path, rar_filename, src_dir)
    try:
        subprocess.call(cmd)
    except Exception, e:
        raise e
        
if __name__ == "__main__":
    winrar("img.rar", "./test2")