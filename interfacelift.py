#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path,os
import re
import urllib.request
import urllib.error
import wget
import subprocess
import sys
import time


res_dict = {
    
    '6400x4000': '/wallpaper/downloads/date/wide_16:10/6400x4000/',
    '5120x3200': '/wallpaper/downloads/date/wide_16:10/5120x3200/',
    '3840x2400': '/wallpaper/downloads/date/wide_16:10/3840x2400/',
    '3360x2100': '/wallpaper/downloads/date/wide_16:10/3360x2100/',
    '2880x1800': '/wallpaper/downloads/date/wide_16:10/2880x1800/',
    '2560x1600': '/wallpaper/downloads/date/wide_16:10/2560x1600/',
    '2304x1440': '/wallpaper/downloads/date/wide_16:10/2304x1440/',
    '2048x1280': '/wallpaper/downloads/date/wide_16:10/2048x1280/',
    '1920x1200': '/wallpaper/downloads/date/wide_16:10/1920x1200/',
    '1680x1050': '/wallpaper/downloads/date/wide_16:10/1680x1050/',
    '1440x900': '/wallpaper/downloads/date/wide_16:10/1440x900/',
    '1280x800': '/wallpaper/downloads/date/wide_16:10/1280x800/',
    '1152x720': '/wallpaper/downloads/date/wide_16:10/1152x720/',
    '1024x640': '/wallpaper/downloads/date/wide_16:10/1024x640/',
    '5120x2880': '/wallpaper/downloads/date/wide_16:9/5120x2880/',
    '3840x2160': '/wallpaper/downloads/date/wide_16:9/3840x2160/',
    '3200x1800': '/wallpaper/downloads/date/wide_16:9/3200x1800/',
    '2880x1620': '/wallpaper/downloads/date/wide_16:9/2880x1620/',
    '2560x1440': '/wallpaper/downloads/date/wide_16:9/2560x1440/',
    '1920x1080': '/wallpaper/downloads/date/wide_16:9/1920x1080/',
    '1024x600': '/wallpaper/downloads/date/wide_16:9/1024x600/',
    '1600x900': '/wallpaper/downloads/date/wide_16:9/1600x900/',
    '1366x768': '/wallpaper/downloads/date/wide_16:9/1366x768/',
    '1280x720': '/wallpaper/downloads/date/wide_16:9/1280x720/',
    '2560x1080': '/wallpaper/downloads/date/wide_21:9/2560x1080/',
    '3440x1440': '/wallpaper/downloads/date/wide_21:9/3440x1440/',
    '6400x3600': '/wallpaper/downloads/date/wide_21:9/6400x3600/',
    '5120x1600': '/wallpaper/downloads/date/2_screens/5120x1600/',
    '5120x1440': '/wallpaper/downloads/date/2_screens/5120x1440/',
    '3840x1200': '/wallpaper/downloads/date/2_screens/3840x1200/',
    '3840x1080': '/wallpaper/downloads/date/2_screens/3840x1080/',
    '3360x1050': '/wallpaper/downloads/date/2_screens/3360x1050/',
    '3200x1200': '/wallpaper/downloads/date/2_screens/3200x1200/',
    '2880x900': '/wallpaper/downloads/date/2_screens/2880x900/',
    '2560x1024': '/wallpaper/downloads/date/2_screens/2560x1024/',
    '7680x1600': '/wallpaper/downloads/date/3_screens/7680x1600/',
    '7680x1440': '/wallpaper/downloads/date/3_screens/7680x1440/',
    '5760x1200': '/wallpaper/downloads/date/3_screens/5760x1200/',
    '5760x1080': '/wallpaper/downloads/date/3_screens/5760x1080/',
    '5040x1050': '/wallpaper/downloads/date/3_screens/5040x1050/',
    '4800x1200': '/wallpaper/downloads/date/3_screens/4800x1200/',
    '4800x900': '/wallpaper/downloads/date/3_screens/4800x900/',
    '4320x900': '/wallpaper/downloads/date/3_screens/4320x900/',
    '4200x1050': '/wallpaper/downloads/date/3_screens/4200x1050/',
    '4096x1024': '/wallpaper/downloads/date/3_screens/4096x1024/',
    '3840x1024': '/wallpaper/downloads/date/3_screens/3840x1024/',
    '3840x960': '/wallpaper/downloads/date/3_screens/3840x960/',
    '3840x720': '/wallpaper/downloads/date/3_screens/3840x720/',
    '3072x768': '/wallpaper/downloads/date/3_screens/3072x768/',
    }

Input = subprocess.getoutput("xrandr | grep -i '*'")
resolution=Input.split()[0]
j=1
print("Your screen resolution is",resolution)

while True:
    down_list=[]
    def download_wallpapers(down_list):
        r=len(down_list)
        print("You are about to download",r,"wallpapers")
        for i in down_list:
            r -=1
            
            print("\nDownloading wallpaper",i[19:])
            wallpaper = wget.download('https://interfacelift.com'+i)
            print("\n")
            if r>0:
                
                print(r,"wallpapers remaining")
                print(" "*50,end="\r")
            else:pass
            
        
    def rss_feed(url):
        url += res_dict[resolution]+"index"+str(j)+".html"
        #url += "widescreen/"+str(resolution)+"/index"+str(j)+".html"
        req = urllib.request.Request(url)
        try:
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('latin-1')
            
            filename = "tempfile.rss"
            with open(filename, "w", encoding="utf-8") as p:
                p.write(html)
        except urllib.error.HTTPError as e:
            print(e.code)
            print(e.readline())
            return 0
        except urllib.error.URLError as e:
            print(e)
            if hasattr(e, 'reason'):  # no internet connection
                print('Failed to connect to the server')
                print('Reason : ', e.reason)
            return 0


    def process_feed(filename):
        with open(filename, 'r', encoding = 'utf-8') as f:
            rss = f.read().replace("\n", " ")
            
            wallpapers = re.findall(r'<a href="(/wallpaper/\w{7,}/\w{5,}.jpg)">',rss, re.I)
            
            
            for i in wallpapers:
                if i[19:] in files_list:
                    print(i[19:],"is already downloaded"+" "*10,end="\r")
                    time.sleep(0.5)
                else:
                    try:
                        down_list.append(i)
                    except UnicodeDecodeError as e:
                        print("\n",e)
                
##                    print("\nDownloading wallpaper",i[19:])
##                    wallpaper = wget.download('https://interfacelift.com'+i)
##                    print(" "*50,end="\r")
                   
            

    url = "https://interfacelift.com/"

    rss_feed(url)
    filename = "tempfile.rss"
    with open(filename, 'r', encoding = 'utf-8') as f:
        rss = f.read().replace("\n", " ")
        
        items = re.findall(r'<b style="color: #bb2f0e;">([0-9]{2,})</b>.</p>',rss, re.I)
        print ("\nThese wallpapers extend in",items[0],"pages")
        time.sleep(1)
        
    while True:
        print("How many pages of the "+items[0]+" do you want to download? \nPress enter if you want to quit")
        try:
            #os.system("clear")
            try:
                start=input("Starting page : ")
                if int(start) not in range(1,int(items[0])+1):
                    print("\nNumber of pages not in range")
                    time.sleep(1)
                    continue
            except ValueError as e:
                if start=="" :
                    break
                
            
            
            #pages=input("How many pages of the "+items[0]+" do you want to download ? \nPress enter if you want to quit : ")
            pages=input("Ending page : ")
            time.sleep(0.5)
            if int(pages) not in range(1,int(items[0])+1):
                print("\nNumber of pages not in range")
                time.sleep(1)
                continue
            if int(pages)<int(start):
                print("Ending page is smaller than the start page, must be at least the same")
            else:
                files_list=[]
                if os.path.exists(resolution) is True:
                     if os.path.isdir(resolution):
                        count_files = 0
                        for r,d,f in os.walk(resolution):
                            level = r.replace(resolution, '').count(os.sep)
                            #print(level*'\t',r)
                            for fi in f:
                                if fi[0] not in '.~':
                                    #print((level+1)*'\t',fi)
                                    files_list.append(fi)
                                    count_files += 1
                        print('There are {} files already downloaded in your folder'.format(count_files))
                        
                        time.sleep(0.5)
                        #print(files_list)
                    
                else:
                    path = os.mkdir(resolution)
                dir = str(os.getcwd()+"/"+str(resolution))
                os.chdir(dir)
                for j in range(int(start),int(pages)+1):
                    
                    rss_feed(url)
                    process_feed(filename)


##                for w in down_list:
##                    print(w)
                download_wallpapers(down_list)
                print("\n\nDone !!!")
                time.sleep(0.5)
                break
        except ValueError as e:
            if pages=="" :
                break
            else:
                print("\nError",e)
                time.sleep(1)
        
    break

os.remove("tempfile.rss")

