#!/usr/bin/python

"""

File: check_mview.py
Author: Ryan Patrick Murphy <ryan.murphy@uni.edu>
Date: 10-14-2015

This script checks the status of the PS materialized views in the CSS Databases and
sends an email if there is a problem.

Currently checks for Materialized Views that need compiled and stale views

Output: An email will be sent if there is a materialized view that needs compiled
or if there is a stale materialized view

"""

import os
from subprocess import Popen,PIPE,STDOUT
import smtplib
import email.utils
from email.mime.text import MIMEText

def main():
  

def run_query(login,sql_file):
  
  cmd = "sqlplus -silent %s @%s" %(login,sql_file)

  p=Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
  
  output,err=p.communicate()

  return output.lstrip('\n').rstrip('\n')
  

def get_login(input_file):

  login_file=open(input_file,'r')
  login=login_file.readline().replace('\n','')
  
  return login


def send_mail(TO,message,subject,database):

  SUBJECT=subject
  FROM = ("PeopleSoft DB Watcher","its-dba+peoplesoft@uni.edu")
  
  msg=MIMEText(message)
  msg['To']=", ".join(TO)
  msg['From']=email.utils.formataddr(FROM)
  msg['Subject']=SUBJECT
  
  server=smtplib.SMTP("mail.uni.edu")
  server.sendmail(FROM, TO, msg.as_string())
  server.quit()
  
  
main()
