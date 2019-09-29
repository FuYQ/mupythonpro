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
    fo=open('E:\\Spark学习\\myPythonproject\\淘宝抓取\\result.txt', mode='a+', encoding='utf-8')
    for img,mingzi,price in zip(imgs,mingzi,price):
        if ll<10:
            img="https://"+img
            fo.writelines(key +"\t"+mingzi+"\t"+price+"\n")
        ll=ll+1
    fo.close();

        # try:
        #     time.sleep(0.2)
        #     file="E:/淘宝图抓取/联合利华/"+str(mingzi)+".jpg"
        #     urllib.request.urlretrieve(img,filename=file)
        #     print("爬取"+str(paqucishu)+"成功")
        #     paqucishu=int(paqucishu)+1
        # except Exception as result:
        #     print('图片下载失败' + str(result))
def get_one_pages():
    keylist=['飞利浦官方旗舰店','比瑞吉旗舰店','TW官方旗舰店','诺优能旗舰店','良品铺子旗舰店','漫花旗舰店','金九旗舰店','王小二旗舰店','水军旗舰店','美即官方旗舰店','skullcandy官方旗舰店','天猫三星官方旗舰店','cuir葵儿化妆品旗舰店','mck旗舰店','ein旗舰店','知味观官方旗舰店','雪肌精官方旗舰店','力士旗舰店','诺瑞旗舰店','烫旗舰店','安耐驰旗舰店','自嗨锅旗舰店','欧普照明官方旗舰店','海尔官方旗舰店','贝妍旗舰店','京东杉杉官方旗舰店','tigrisso旗舰店','女巫和骑士旗舰店','isdg海外旗舰店','杏花楼食品旗舰店','POLA海外旗舰店','胜道官方旗舰店','易果旗舰店','三星家电旗舰店','汇仁官方旗舰店','嘉华食品旗舰店','千趣会官方旗舰店','大麦网官方旗舰店','波顿旗舰店','顶瓜瓜品牌旗舰店','半亩花田旗舰店','妮维雅旗舰店','goodhealth海外旗舰店','蒂可伊服饰旗舰店','MDC海外旗舰店','路斯旗舰店','淘宝搜索广州酒家旗舰店','锦度旗舰店','清风官方旗舰店','凌丹娜旗舰店','耐威克官方旗舰店','新雅食品旗舰店','马拉丁官方旗舰店','CANIDAE卡比海外旗舰店','海俪恩隐形眼镜旗舰店','米旗官方旗舰店','铭果世嘉旗舰店','牛百岁旗舰店','WIS旗舰店','宽福旗舰店','荣华食品旗舰店','冒个泡旗舰店','古磨坊旗舰店','启初旗舰店','布朗舒格旗舰店','潮香村食品旗舰店','美味连连生鲜旗舰店','兴盛旗舰店','ZUCZUG官方旗舰店','ampleur海外旗舰店','露安适官方旗舰店','冠能官方旗舰店','左颜右色旗舰店','特步官方旗舰店','雅培海外旗舰店','绽妍旗舰店','乐麦点旗舰店','猫太子数码旗舰店','ilovechoc旗舰店','江南先生旗舰店','UH化妆品旗舰店','钓鱼王旗舰店','pasok旗舰店','ASICS旗舰店','PANMAX旗舰店','海尔曼斯旗舰店','回头客食品旗舰店','佰草集官方旗舰店','zhr旗舰店','鲜汇居旗舰店','真皙旗舰店','honeycare旗舰店','漫娱文化图书旗舰店','金三塔内衣旗舰店','谷登旗舰店','麦迪王子旗舰店','伊利冰淇淋旗舰店','周五五旗舰店','上水井食品旗舰店','春纪旗舰店','52025内衣旗舰店','荣诚旗舰店','李医生化妆品旗舰店','物生物旗舰店','速品旗舰店','好之味官方旗舰店','快乐跑官方旗舰店','天美意官方旗舰店','lumi旗舰店','金利来女包旗舰店','暇步士官方旗舰店','德佑旗舰店','浙西徐香旗舰店','柏品旗舰店','舒达源天猫旗舰店','思味王食品旗舰店','味多美旗舰店','天衡宝旗舰店','慕思旗舰店','pokee旗舰店','四洲食品旗舰店','nexyco奈蔻旗舰店','途虎官方旗舰店','lalabobo旗舰店','中粮食品旗舰店','我龙旗舰店','惠氏海外旗舰店','HARRIET海瑞特旗舰店','美斯蒂克海外旗舰店','多彩丽人旗舰店','爱宝乐母婴旗舰店','it官方旗舰店','medicura海外旗舰店','波力官方旗舰店','a1爱逸旗舰店','jifro洁芙柔旗舰店','earthsbest旗舰店','keheal旗舰店','RedBull海外旗舰店','善必征大药房旗舰店','凰朝滋补堂旗舰店','mytex旗舰店','初语旗舰店','极宠家旗舰店','京东天美意旗舰店','金苑旗舰店','魔香旗舰店','TUMI旗舰店','lackpard旗舰店','kon旗舰店','丽人丽妆海外旗舰店','得欧娜女鞋旗舰店','德德维芙旗舰店','禾甘旗舰店','耐吉斯宠物食品旗舰店','岭南新宝堂旗舰店','恬梦莱旗舰店','Libresse旗舰店','YEE官方旗舰店','荣耀官方旗舰店','健得乐旗舰店','思乐智旗舰店','十月结晶旗舰店','策括旗舰店','派邦奴旗舰店','京润珍珠旗舰店','scofield官方旗舰店','kakaofriends旗舰店','鸿星尔克官方旗舰店','allolugh旗舰店','森田官方旗舰店','orgain海外旗舰店','伊肤泉旗舰店','GNC海外旗舰店','芊动旗舰店','彼思旗舰店','TOVAOON旗舰店','橙乐工坊旗舰店','巧帛旗舰店','永璞旗舰店','nautica童装旗舰店','康宝旗舰店','道易鑫物联网旗舰店','森达官方旗舰店','爱视杰旗舰店','圣地莱旗舰店','巧罗旗舰店','壹念旗舰店','双沟官方旗舰店','ENEOMEY海外旗舰店','蒂洛克旗舰店','欧力姆旗舰店','珍尚米旗舰店','四皓食品旗舰店','肌肉科技海外旗舰店','御泥坊旗舰店','凯乐石旗舰店']
    # keylist=['联合利华旗舰店','3CE官方旗舰店','波奇网旗舰店']
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