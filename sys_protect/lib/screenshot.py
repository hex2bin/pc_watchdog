#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename: ScreenShot.py
# History:
#   1, 2012-05-09, created.

"""
This is based on Nircmd.exe program.
"""

import os
import subprocess
import time

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger("Screen_shot")
    
def save_screen(img_path=None, delay=None, img_format="bmp"):
    """
    Save the current screen to a image file.
    Support png, bmp, jpg etc image file format.
    Accoding the suffix to generate image format.
    Default is bmp.
    
    Arguments:
    img_path    the specified path to save a image file.
    delay       wait delay milliseconds to save screen.
    
    Usage example:      save_screen("D:\\test.bmp", 2000)
    """

    file_path   = os.path.dirname(__file__)
    abs_path    = os.path.abspath(file_path)
    
    if img_path is None or\
        not os.path.exists(os.path.dirname(img_path)):
        time_stamp  = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        filename    = "Nircmd-" + time_stamp + "." + img_format
        img_path    = abs_path + "\\" + filename
        # print "img file_path:%s" % img_path
        
    elif os.path.exists(img_path):
        time_stamp  = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        filename    = "Nircmd-" + time_stamp + "." + img_format
        img_path    = img_path + "\\" + filename
    
    if delay is None:
        delay = 0
    
    try:
        cmd_path = abs_path + "\\" + "Nircmd.exe"
        # print "Nircmd.exe file path:%s" % cmd_path
        cmd = '''%s cmdwait %d savescreenshot "%s"''' % (cmd_path, delay, img_path)
        subprocess.call(cmd)
        # print "save a screen to %s" % img_path
        # logger.info("save a screen to %s" % img_path)
    except Exception, e:
        # logger.error("Save screen failed: %s" % e)
        raise e
        
if __name__ == "__main__":
    save_screen(r'G:\stor_evn_ipc\lib\tt')
        