# coding=gbk
import re
import time
import urllib.request

import requests
from bs4 import BeautifulSoup

headers={
    'cookie' : 'miid=1296267545453648768; t=b4d385e2145f596a67961e4dd08e9a8f; cna=pqwcFXxbJjACAXWIA7AFEfA8; thw=cn; tracknick=tb487881011; lgc=tb487881011; _cc_=UIHiLt3xSw%3D%3D; tg=0; enc=%2FTqA3gAexHOKU0cyPYbSWM1pGS8vgnlEK3EMnkYd2T%2BlB%2BJh18hxryREG48c%2BYmdk7yfvbSMCBDQExP23eUm3w%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; cookie2=19ef67fdfc3f433776e5e9cafaf6a8ea; v=0; _tb_token_=08b7e3e7e183; _m_h5_tk=62383241b06635c64b07942e50e47d9d_1562004576179; _m_h5_tk_enc=0465da475a8335f8fd8d9ef6bb280a71; unb=4235284520; sg=101; _l_g_=Ug%3D%3D; skt=c571ae590b7580cb; cookie1=AnQIvxj44XbyESoVNTVtwfJRB8W%2BbAPV%2BVZMWhAghjk%3D; csg=23f40375; uc3=vt3=F8dBy34cs3fc7ebsEqk%3D&id2=Vy67WD1MZomrsw%3D%3D&nk2=F5RBzeKtOazPVJc%3D&lg2=UtASsssmOIJ0bQ%3D%3D; existShop=MTU2MTk5NTE3MQ%3D%3D; dnk=tb487881011; _nk_=tb487881011; cookie17=Vy67WD1MZomrsw%3D%3D; mt=ci=21_1; uc1=cookie14=UoTaGdT0tHdY5w%3D%3D&lng=zh_CN&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie21=VFC%2FuZ9aj3yE&tag=8&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0; whl=-1%260%260%261561995222497; isg=BHNzJqpkKgCWtOesccf13ZRUAnddACwkF8iwAyUQzxLJJJPGrXiXutG23hRvn19i; l=bBMxcfBPv539-OTkBOCanurza77OSIRYYuPzaNbMi_5K-6T_2qQOkAuQFF96Vj5Rs4YB4G2npwJ9-etkq',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

paqucishu=0
def get_one_page(url,key):
    url.encode("UTF-8")
    # print(url)
    urls=requests.get(url,headers=headers)
    urls=urls.text.encode("UTF-8")
    # print(url)
    # print(urls)
    soup=BeautifulSoup(urls,"html.parser")
    # print(soup)
    print(soup)
    zhengze='"pic_url":"//(.*?)",'
    zhengze_mingzi='"raw_title":"(.*?)",'
    zhengze_price='"view_price":"([0-9]+\\.[0-9]+?)",'
    imgs=re.compile(zhengze).findall(str(soup))
    mingzi=re.compile(zhengze_mingzi).findall(str(soup))
    price=re.compile(zhengze_price).findall(str(soup))

    global paqucishu
    ll=0
    fo=open('E:\\Sparkѧϰ\\myPythonproject\\�Ա�ץȡ\\result.txt', mode='a+', encoding='utf-8')
    for img,mingzi,price in zip(imgs,mingzi,price):
        if ll<10:
            img="https://"+img
            fo.writelines(key +"\t"+mingzi+"\t"+price+"\n")
        ll=ll+1
    fo.close();

        # try:
        #     time.sleep(0.2)
        #     file="E:/�Ա�ͼץȡ/��������/"+str(mingzi)+".jpg"
        #     urllib.request.urlretrieve(img,filename=file)
        #     print("��ȡ"+str(paqucishu)+"�ɹ�")
        #     paqucishu=int(paqucishu)+1
        # except Exception as result:
        #     print('ͼƬ����ʧ��' + str(result))
def get_one_pages():
    keylist=['�����ֹٷ��콢��','�����콢��','TW�ٷ��콢��','ŵ�����콢��','��Ʒ�����콢��','�����콢��','����콢��','��С���콢��','ˮ���콢��','�����ٷ��콢��','skullcandy�ٷ��콢��','��è���ǹٷ��콢��','cuir������ױƷ�콢��','mck�콢��','ein�콢��','֪ζ�۹ٷ��콢��','ѩ�����ٷ��콢��','��ʿ�콢��','ŵ���콢��','���콢��','���ͳ��콢��','���˹��콢��','ŷ�������ٷ��콢��','�����ٷ��콢��','�����콢��','����ɼɼ�ٷ��콢��','tigrisso�콢��','Ů�׺���ʿ�콢��','isdg�����콢��','�ӻ�¥ʳƷ�콢��','POLA�����콢��','ʤ���ٷ��콢��','�׹��콢��','���Ǽҵ��콢��','���ʹٷ��콢��','�λ�ʳƷ�콢��','ǧȤ��ٷ��콢��','�������ٷ��콢��','�����콢��','���Ϲ�Ʒ���콢��','��Ķ�����콢��','��ά���콢��','goodhealth�����콢��','�ٿ��������콢��','MDC�����콢��','·˹�콢��','�Ա��������ݾƼ��콢��','�����콢��','���ٷ��콢��','�赤���콢��','�����˹ٷ��콢��','����ʳƷ�콢��','�������ٷ��콢��','CANIDAE���Ⱥ����콢��','��ٳ�������۾��콢��','����ٷ��콢��','���������콢��','ţ�����콢��','WIS�콢��','���콢��','�ٻ�ʳƷ�콢��','ð�����콢��','��ĥ���콢��','�����콢��','��������콢��','�����ʳƷ�콢��','��ζ���������콢��','��ʢ�콢��','ZUCZUG�ٷ��콢��','ampleur�����콢��','¶���ʹٷ��콢��','���ܹٷ��콢��','������ɫ�콢��','�ز��ٷ��콢��','���ຣ���콢��','�����콢��','������콢��','è̫�������콢��','ilovechoc�콢��','���������콢��','UH��ױƷ�콢��','�������콢��','pasok�콢��','ASICS�콢��','PANMAX�콢��','������˹�콢��','��ͷ��ʳƷ�콢��','�۲ݼ��ٷ��콢��','zhr�콢��','�ʻ���콢��','����콢��','honeycare�콢��','�����Ļ�ͼ���콢��','�����������콢��','�ȵ��콢��','��������콢��','����������콢��','�������콢��','��ˮ��ʳƷ�콢��','�����콢��','52025�����콢��','�ٳ��콢��','��ҽ����ױƷ�콢��','�������콢��','��Ʒ�콢��','��֮ζ�ٷ��콢��','�����ܹٷ��콢��','������ٷ��콢��','lumi�콢��','������Ů���콢��','Ͼ��ʿ�ٷ��콢��','�����콢��','���������콢��','��Ʒ�콢��','���Դ��è�콢��','˼ζ��ʳƷ�콢��','ζ�����콢��','��ⱦ�콢��','Ľ˼�콢��','pokee�콢��','����ʳƷ�콢��','nexyco��ޢ�콢��',';���ٷ��콢��','lalabobo�콢��','����ʳƷ�콢��','�����콢��','���Ϻ����콢��','HARRIET�������콢��','��˹�ٿ˺����콢��','��������콢��','������ĸӤ�콢��','it�ٷ��콢��','medicura�����콢��','�����ٷ��콢��','a1�����콢��','jifro��ܽ���콢��','earthsbest�콢��','keheal�콢��','RedBull�����콢��','�Ʊ�����ҩ���콢��','�˳��̲����콢��','mytex�콢��','�����콢��','������콢��','�����������콢��','��Է�콢��','ħ���콢��','TUMI�콢��','lackpard�콢��','kon�콢��','������ױ�����콢��','��ŷ��ŮЬ�콢��','�µ�άܽ�콢��','�̸��콢��','�ͼ�˹����ʳƷ�콢��','�����±����콢��','�������콢��','Libresse�콢��','YEE�ٷ��콢��','��ҫ�ٷ��콢��','�������콢��','˼�����콢��','ʮ�½ᾧ�콢��','�����콢��','�ɰ�ū�콢��','���������콢��','scofield�ٷ��콢��','kakaofriends�콢��','���Ƕ��˹ٷ��콢��','allolugh�콢��','ɭ��ٷ��콢��','orgain�����콢��','����Ȫ�콢��','GNC�����콢��','ܷ���콢��','��˼�콢��','TOVAOON�콢��','���ֹ����콢��','�ɲ��콢��','����콢��','nauticaͯװ�콢��','�����콢��','�������������콢��','ɭ��ٷ��콢��','���ӽ��콢��','ʥ�����콢��','�����콢��','Ҽ���콢��','˫���ٷ��콢��','ENEOMEY�����콢��','������콢��','ŷ��ķ�콢��','�������콢��','���ʳƷ�콢��','����Ƽ������콢��','���෻�콢��','����ʯ�콢��']
    # keylist=['���������콢��','3CE�ٷ��콢��','�������콢��']
    for k in range(0,len(keylist)):
        key = keylist[k]
        # print(key)
        key_name=urllib.request.quote(key)
        url="https://s.taobao.com/search?q="+key_name+"&s="+str(int(0)*44)
        print(url)
        time.sleep(1)
        get_one_page(url,key)

if __name__ == '__main__':
    # print(os.getcwd())
    get_one_pages()