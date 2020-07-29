
from requests import get
from bs4 import BeautifulSoup
from os import path,mkdir
import datetime
a=datetime.date(2020,7,20)
for i in range(0,10):
    a=a-datetime.timedelta(days=1)
    a.strftime('%Y%m%d')
    res=get('https://bing.wallpaper.pics/CN/'+a.strftime('%Y%m%d')+'.html')
    soup=BeautifulSoup(res.text,'html.parser')
    lab=soup.find(name='img')
    b=lab.get('src').split('=')[1][0:-17]
    url='https://cn.bing.com/th?id='+b+'_UHD.jpg&rf=LaDigue_UHD.jpg&pid=hp&w=3840&h=2160&rs=1&c=4'
    c=a.strftime('%Y%m%d')+'.jpg'
    if path.exists('xxx') is False:
        mkdir('xxx')
    imagefile=open(path.join('xxx',c),'wb')
    for chunk in get(url).iter_content():
        imagefile.write(chunk)
    imagefile.close()