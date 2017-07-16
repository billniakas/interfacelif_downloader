import os.path
import re
import urllib.request
import urllib.error
import wget
import subprocess
import sys
Input = subprocess.getoutput("xrandr | grep -i '*'")
resolution=Input.split()[0]
j=1
print("Your screen resolution is ",resolution)
print("^^^^^^^^^^^^^^^^^^^^^^^")
while True:
    def rss_feed(url):
        url += "widescreen/"+str(resolution)+"/index"+str(j)+".html"
        req = urllib.request.Request(url)
        try:
            with urllib.request.urlopen(req) as response:
                html = response.read().decode()
            
            filename = "tempfile.rss"
            with open(filename, "w", encoding="utf-8") as p:
                p.write(html)
        except urllib.error.HTTPError as e:
            print(e.code)
            print(e.readline())
            return 0
        except urllib.error.URLError as e:
            print(e)
            if hasattr(e, 'reason'):  # χωρίς σύνδεση ιντερνετ
                print('Failed to connect to the server')
                print('Reason : ', e.reason)
            return 0
    ##    else:
    ##        if (process_feed(filename)) : return 1
    ##        else : return 0

    def process_feed(filename):
            
        with open(filename, 'r', encoding = 'utf-8') as f:
            rss = f.read().replace("\n", " ")
            #feeds = []
            #items = re.findall(r'<b style="color: #bb2f0e;">([0-9]{2,})</b>.</p>',rss, re.I)

            #print ("These wallpapers extend in",items[0],"pages")
           
            wallpapers = re.findall(r'<a href="(/wallpaper/\w{7}/\w{5,}.jpg)',rss, re.I)
            
            for i in wallpapers:
               
                print(i)
                wallpaper = wget.download('https://interfacelift.com'+i)
                
        
            

    url = "https://interfacelift.com/wallpaper/downloads/date/"

    rss_feed(url)
    filename = "tempfile.rss"
    with open(filename, 'r', encoding = 'utf-8') as f:
        rss = f.read().replace("\n", " ")
        feeds = []
        items = re.findall(r'<b style="color: #bb2f0e;">([0-9]{2,})</b>.</p>',rss, re.I)

        print ("These wallpapers extend in",items[0],"pages")


    pages=input("How many pages of the "+items[0]+" do you want to download ? \nPress enter if you want to quit : ")
    if pages=="": break
    else:
        

        if os.path.exists(resolution) is True:
            pass
        else:
            path = os.mkdir(resolution)
        dir = str(os.getcwd()+"/"+str(resolution))
        os.chdir(dir)
        for j in range(1,int(pages)+1):
            
            rss_feed(url)
            process_feed(filename)
       


os.remove("tempfile.rss")
