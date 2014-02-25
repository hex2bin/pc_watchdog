#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename: sendmail.py
# 

import os
import sys
import smtplib
import email

class SendMail(object):
    def __init__(self, dst_mail=None, src_mail=None):
        self.mail = email.MIMEMultipart.MIMEMultipart()
        
        self.dst_mail = dst_mail
        self.src_mail = src_mail
        
        self.subject = None
        self.content = None
        self.att = None
        
    def add_subject(self, subject):
        self.mail['subject'] = email.Header.Header(subject, 'cp936')
        
    def add_content(self, content):
        self.content = email.MIMEText.MIMEText(content, 'plain', 'cp936')
        self.mail.attach(self.content)
        
    def add_attch(self, filename):
        self.basename = os.path.basename(filename)
        
        self.att = email.MIMEText.MIMEText(open(filename, 'rb').read(), 'base64', 'CP936')  
        self.att["Content-Type"]        = 'application/octet-stream'
        self.att["Content-Disposition"] = 'attachment; filename=%s' % self.basename.encode('CP936')
        
        self.mail.attach(self.att)
        
    def send_mail(self, mail_host, username, password, dst_mail=None, src_mail=None):
        if self.dst_mail is None and dst_mail is None:
            print "Please sepcified a destination mail address."
            sys.exit(0)
        elif dst_mail is not None:
            self.dst_mail = dst_mail
        else:
            pass
        
        self.mail["to"]     = ";".join(self.dst_mail)
        self.mail["from"]   = self.src_mail
        
       
        my_send = smtplib.SMTP(mail_host, 587)
        my_send.ehlo()
        my_send.starttls()
        # my_send.set_debuglevel(1)
        my_send.login(username, password)
        
        my_send.sendmail(self.mail["from"], self.dst_mail, self.mail.as_string())
        # my_send.sendmail(self.mail["from"], self.mail["to"], self.mail.as_string())
        my_send.close()
        
        
if __name__ == "__main__":
    subject  = "Re: Re: Re: [MISC]©зд╬"
    content  = "XXXX.."
    my = SendMail(dst_list, src_list)
    my.add_subject(subject)
    my.add_content(content)