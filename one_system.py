# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 14:05:56 2018

@author: Nicholas Ioannidis
"""

import serial
import time
import csv
from datetime import datetime as dtt
import pandas as pd

count = 0

DOPEY = serial.Serial('COM14',9600)
DOC = serial.Serial('COM23',9600)
BASHFUL = serial.Serial('COM20',9600)
GRUMPY = serial.Serial('COM8',9600)
SNEEZY = serial.Serial('COM21',9600)
SLEEPY = serial.Serial('COM11',9600)
HAPPY = serial.Serial('COM18',9600)
    
while True:
    try:
        
        if(count == 10):
            
               now = dtt.now()
               BASHFUL.write(b'1')
               BASHFUL.flushInput()
               bashful_total = []

               for x in range(5):
                   bashful_val = BASHFUL.readline()
                   bashful_total.append(float(bashful_val[0:len(bashful_val)-2].decode("utf-8")))
                   time.sleep(0.1)
               print('Bashful')
               for k in range(5):
                   print(bashful_total[k])
                   time.sleep(0.2)
               time.sleep(0.2)
               time.sleep(2)
               
               GRUMPY.write(b'1')
               GRUMPY.flushInput()
               grumpy_total = []

               for x in range(5):
                   grumpy_val = GRUMPY.readline()
                   grumpy_total.append(float(grumpy_val[0:len(grumpy_val)-2].decode("utf-8")))
                   time.sleep(0.1)
               
    
            
               print('Grumpy')
    
               for k in range(5):
                   print(grumpy_total[k])
                   time.sleep(0.2)
               time.sleep(0.2)
               time.sleep(2)
               
               DOPEY.write(b'1')
               DOPEY.flushInput()
               dopey_total = []

               for x in range(5):
                   dopey_val = DOPEY.readline()
                   dopey_total.append(float(dopey_val[0:len(dopey_val)-2].decode("utf-8")))
                   time.sleep(0.1)
               print('Dopey')
               for k in range(5):
                   print(dopey_total[k])
                   time.sleep(0.2)
               time.sleep(2)
               
               SNEEZY.write(b'1')
               SNEEZY.flushInput()
               sneezy_total = []

               for x in range(5):
                   sneezy_val = SNEEZY.readline()
                   sneezy_total.append(float(sneezy_val[0:len(sneezy_val)-2].decode("utf-8")))
                   time.sleep(0.1)
               print('Sneezy')
               for k in range(5):
                   print(sneezy_total[k])
                   time.sleep(0.2)
               time.sleep(2)
                   
               SLEEPY.write(b'1')
               SLEEPY.flushInput()
               sleepy_total = []

               for x in range(5):
                   sleepy_val = SLEEPY.readline()
                   sleepy_total.append(float(sleepy_val[0:len(sleepy_val)-2].decode("utf-8")))
                   time.sleep(0.1)
               print('Sleepy')
               for k in range(5):
                   print(sleepy_total[k])
                   time.sleep(0.2)
               time.sleep(2)
                   
               HAPPY.write(b'1')
               HAPPY.flushInput()
               happy_total = []

               for x in range(5):
                   happy_val = HAPPY.readline()
                   happy_total.append(float(happy_val[0:len(happy_val)-2].decode("utf-8")))
                   time.sleep(0.1)
               print('Happy')
               for k in range(5):
                   print(happy_total[k])
                   time.sleep(0.2)
               time.sleep(2)
                   
               DOC.write(b'1')
               DOC.flushInput()
               doc_total = []

               for x in range(5):
                   doc_val = DOC.readline()
                   doc_total.append(float(doc_val[0:len(doc_val)-2].decode("utf-8")))
                   time.sleep(0.1)
               print('Doc')
               for k in range(5):
                   print(doc_total[k])
                   time.sleep(0.2)
               count = 0
               
        count+=1
        time.sleep(1)   
    except KeyboardInterrupt:
        BASHFUL.close()
        time.sleep(0.1)
        GRUMPY.close()
        time.sleep(0.1)
        DOPEY.close()
        time.sleep(0.1)
        SNEEZY.close()
        time.sleep(0.1)
        SLEEPY.close()
        time.sleep(0.1)
        HAPPY.close()
        time.sleep(0.1)
        DOC.close()
        time.sleep(0.1)
        
        print("Data Saved!")
        break




    