from requests import get
from bs4 import BeautifulSoup
from os import path,mkdir
import time
import win32api
import win32con
import win32gui


res=get('https://cn.bing.com/')
soup=BeautifulSoup(res.text,'html.parser')
lab=soup.find(name='div',attrs={'id':'bgImgProgLoad'})
a='https://cn.bing.com'+lab.get('data-ultra-definition-src')
res=get(a.replace('w=1920&h=1080','w=3840&h=2160'))
day=time.strftime('%Y-%m-%d',time.localtime(time.time()))
c=day+'.jpg'
if path.exists('xxx') is False:
    mkdir('xxx')
imagefile=open(path.join('xxx',c),'wb')
for chunk in res.iter_content():
    imagefile.write(chunk)
imagefile.close()
def setWallpaper(image_path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,image_path, 1+2)
setWallpaper(path.join('D:/PycharmProjects/wallpaper/xxx',c))