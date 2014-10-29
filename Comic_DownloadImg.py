import urllib
import time
import HTMLParser
import re
import time

'''
test_str = "\"werwfehhttp://cartoon.jide123.cc/manhuatuku/7081/comicdata3_r_rxgx_006_002czvuawh.jpgewfasjpgd\";\n"
 
print re.findall("http://cartoon.jide123.cc.*?.jpg", test_str)[0]
    while (len(re.findall("http://cartoon.jide123.cc.*?.jpg", html)) == 0):
            time.sleep(0.1)
            html = f.read()
        imgurl = re.findall("http://cartoon.jide123.cc.*?.jpg", html)[0]
        f.close()
        name = r("" + str(i) + ".jpg")
        #imgurl = r"http://cartoon.jide123.cc/manhuatuku/7081/comicdata3_r_rxgx_006_002czvuawh.jpg"  #path = "d:/python1" +'//'+name
        urllib.urlretrieve(imgurl,name)   #s=urllib.urlretrieve(url,path)
'''
def main():
    logfile = 'osamu8.urls.log'
    with open(logfile) as f:
        for imgurl in f:
            print imgurl
            imgurl = imgurl.strip()
            img = imgurl[imgurl.find("comic"):]
            urllib.urlretrieve(imgurl,img)
 
       
if __name__ == "__main__":
    main()

