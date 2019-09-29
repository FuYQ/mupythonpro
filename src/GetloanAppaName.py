import re
import time
import urllib.request

import requests
from bs4 import BeautifulSoup

headers={
    'cookie' : 'miid=1296267545453648768; t=b4d385e2145f596a67961e4dd08e9a8f; cna=pqwcFXxbJjACAXWIA7AFEfA8; thw=cn; tracknick=tb487881011; lgc=tb487881011; _cc_=UIHiLt3xSw%3D%3D; tg=0; enc=%2FTqA3gAexHOKU0cyPYbSWM1pGS8vgnlEK3EMnkYd2T%2BlB%2BJh18hxryREG48c%2BYmdk7yfvbSMCBDQExP23eUm3w%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; cookie2=19ef67fdfc3f433776e5e9cafaf6a8ea; v=0; _tb_token_=08b7e3e7e183; _m_h5_tk=62383241b06635c64b07942e50e47d9d_1562004576179; _m_h5_tk_enc=0465da475a8335f8fd8d9ef6bb280a71; unb=4235284520; sg=101; _l_g_=Ug%3D%3D; skt=c571ae590b7580cb; cookie1=AnQIvxj44XbyESoVNTVtwfJRB8W%2BbAPV%2BVZMWhAghjk%3D; csg=23f40375; uc3=vt3=F8dBy34cs3fc7ebsEqk%3D&id2=Vy67WD1MZomrsw%3D%3D&nk2=F5RBzeKtOazPVJc%3D&lg2=UtASsssmOIJ0bQ%3D%3D; existShop=MTU2MTk5NTE3MQ%3D%3D; dnk=tb487881011; _nk_=tb487881011; cookie17=Vy67WD1MZomrsw%3D%3D; mt=ci=21_1; uc1=cookie14=UoTaGdT0tHdY5w%3D%3D&lng=zh_CN&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie21=VFC%2FuZ9aj3yE&tag=8&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0; whl=-1%260%260%261561995222497; isg=BHNzJqpkKgCWtOesccf13ZRUAnddACwkF8iwAyUQzxLJJJPGrXiXutG23hRvn19i; l=bBMxcfBPv539-OTkBOCanurza77OSIRYYuPzaNbMi_5K-6T_2qQOkAuQFF96Vj5Rs4YB4G2npwJ9-etkq',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
url="https://s.taobao.com/search?q=%E9%A3%9E%E5%88%A9%E6%B5%A6%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&s=0"
url.encode("UTF-8")
# print(url)
urls=requests.get(url,headers=headers)
# print(urls.text)
urls=urls.text.encode("UTF-8")
# print(urls)
soup=BeautifulSoup(urls,"html.parser")
print(soup)
zztitile='"title":"(.*)"'
zzdowntimes='"app-btn":"(.*)"'
titilename=re.compile(zztitile).findall(str(soup))
downtimes = re.compile(zzdowntimes).findall(str(soup))
for title,times,price in zip(titilename,downtimes):
    print(title+":"+times)
# print(soup)
# zhengze='"pic_url":"//(.*?)",'
# zhengze_mingzi='"raw_title":"(.*?)",'
# zhengze_price='"view_price":"([0-9]+\\.[0-9]+?)",'
# imgs=re.compile(zhengze).findall(str(soup))
# mingzi=re.compile(zhengze_mingzi).findall(str(soup))
# price=re.compile(zhengze_price).findall(str(soup))