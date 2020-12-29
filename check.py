#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-
"""
    @Description: Check if the browser installed correctly.
    
    ~~~~~~ 
    @Author  : longwenzhang
    @Time    : 19-10-29   3:46
"""
import urllib.request, urllib.error, urllib.parse

from selenium import webdriver
from util import print_info, print_warn

def check_install():
    try:
        br=webdriver.Chrome()
    except Exception as e:
        print(e)
        try:
            br=webdriver.PhantomJS()
        except Exception as e:
            print(e)
            print_warn('No browser is installed correctly!')
        else:
            br.quit()
            print_info('Phantomjs is installed correctly.')
    else:
        br.quit()
        print_info('Chrome is installed correctly.')
        try:
            br=webdriver.PhantomJS()
        except Exception as e:
            print(e)
        else:
            br.quit()
            print_info('Phantomjs is installed correctly.')
    exit(0)

def check_url(url):
    try:
        urllib.request.urlopen(url,timeout=20)
    except Exception as e:
        print('Check url error: '+str(e))
        exit(0)
