#!/usr/bin/python
#-*- encoding: utf-8 -*-
#author : rayment
#CreateDate : 2013-01-24

import imaplib
import email
#������������ʹ�����ı���
import sys
import os
import thread
import time

import my_zipfile

reload(sys)
sys.setdefaultencoding('gbk')

start_date = 20140221000000

mail_filter_lst = ['''(FROM 'test@test.net')''', '''(FROM 'idsinglefunny@gmail.com')''', '''(FROM "mailer-daemon@googlemail.com")''']

#�����ļ����������Ǳ�����ָ���ĸ�Ŀ¼�£�
def savefile(filename, data, path):
    try:
        # filepath = path + filename
        filepath = os.path.join(path, filename)
        print 'Saved as ' + filepath
        f = open(filepath, 'wb')
    except:
        print('filename error')
        f.close()
    f.write(data)
    f.close()
   
#�ַ�����ת������
def my_unicode(s, encoding):
    if encoding:
        return unicode(s, encoding)
    else:
        return unicode(s)

#����ַ����뷽��
def get_charset(message, default="ascii"):
    #Get the message charset
    return message.get_charset()
    return default

#�����ʼ����������ֳ������븽����
def parseEmail(msg, mypath):
    mailContent = None
    contenttype = None
    suffix =None
    for part in msg.walk():
        if not part.is_multipart():
            contenttype = part.get_content_type()   
            filename = part.get_filename()
            charset = get_charset(part)
            #�Ƿ��и���
            if filename:
                h = email.Header.Header(filename)
                dh = email.Header.decode_header(h)
                fname = dh[0][0]
                encodeStr = dh[0][1]
                if encodeStr != None:
                    if charset == None:
                        fname = fname.decode(encodeStr, 'gbk')
                    else:
                        fname = fname.decode(encodeStr, charset)
                data = part.get_payload(decode=True)
                print('Attachment : ' + fname)
                #���渽��
                if fname != None or fname != '':
                    if fname.endswith("ct"):
                        savefile(fname, data, mypath)
                        if int(fname[:-3].replace("-", "")) >= start_date:
                            # my_zipfile.unzip_file(os.path.join(mypath, fname), r'E:\sys_protect\test2\%s' % fname[:10])
                            thread.start_new_thread(my_zipfile.unzip_file, (os.path.join(mypath, fname), r'E:\sys_protect\test2\%s' % fname[:10]))
            else:
                if contenttype in ['text/plain']:
                    suffix = '.txt'
                if contenttype in ['text/html']:
                    suffix = '.htm'
                if charset == None:
                    mailContent = part.get_payload(decode=True)
                else:
                    mailContent = part.get_payload(decode=True).decode(charset)         
    return  (mailContent, suffix)

#��ȡ�ʼ�����
def getMail(mailhost, account, password, diskroot, port = 993, ssl = 1):
    # mypath = diskroot + ':\\'
    mypath = diskroot
    
    
    #�Ƿ����ssl
    if ssl == 1:
        imapServer = imaplib.IMAP4_SSL(mailhost, port)
    else:
        imapServer = imaplib.IMAP4(mailhost, port)
    imapServer.login(account, password)
    imapServer.select()
    
    #�ʼ�״̬���ã����ʼ�ΪUnseen
    #Message statues = 'All,Unseen,Seen,Recent,Answered, Flagged'
    
    for mail_filter in mail_filter_lst:
        resp, items = imapServer.search(None, mail_filter, "UNSEEN")
        # resp, items = imapServer.search(None, "UNSEEN")
        number = 1
        for i in items[0].split():
           #get information of email
           resp, mailData = imapServer.fetch(i, "(RFC822)")   
           mailText = mailData[0][1]
           msg = email.message_from_string(mailText)
           ls = msg["From"].split(' ')
           strfrom = ''
           if(len(ls) == 2):
               fromname = email.Header.decode_header((ls[0]).strip('\"'))
               strfrom = 'From : ' + my_unicode(fromname[0][0], fromname[0][1]) + ls[1]
           else:
               strfrom = 'From : ' + msg["From"]
           strdate = 'Date : ' + msg["Date"]
           subject = email.Header.decode_header(msg["Subject"])
           sub = my_unicode(subject[0][0], subject[0][1])
           strsub = 'Subject : ' + sub
                 
           mailContent, suffix = parseEmail(msg, mypath)
           #���������ʼ�������Ϣ
           print '\n'
           print 'No : ' + str(number)
           print strfrom
           print strdate
           print strsub
           '''
           print 'Content:'
           print mailContent
           '''
           #�����ʼ�����
           if (suffix != None and suffix != '') and (mailContent != None and mailContent != ''):
               # savefile(str(number) + suffix, mailContent, mypath)
               number = number + 1
           
           # imapServer.store(i, '+FLAGS', '\\Deleted')
       
       
    imapServer.close()
    imapServer.logout()


if __name__ =="__main__":

    #�ʼ�������e��
    mypath =r'E:\sys_protect\test'
    
    
    
    while True:
        print 'begin to get email...'
        getMail('pop.gmail.com', 'idsinglefunny@gmail.com', 'id1t2j3k', mypath, 993, 1)
        #126�����½û��ssl
        #getMail('imap.126.com', 'xxxxxxxxx@126.com', 'xxxxxxxxxx', mypath, 143, 0)
        print 'the end of get email.'
        
        
        print 'sleep 1 hour'
        # att_lst = os.listdir(mypath)
        
            
        time.sleep(3600)