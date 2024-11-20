# 目标网站MyLiveWallpapers   url地址  https://wallpaperwaifu.com/  翻页参数 page/数字/
import time

import requests
from lxml import etree
import os

pdda = 1
def mk_create():
    mk = './WallpaperWaifu爬虫数据/图片/第%d页' % pdda
    if not os.path.exists(mk):
        os.makedirs(mk)
    return mk
while True:
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
        'Referer':'https://wallpaperwaifu.com/page/%d/' % (pdda),
    }
    response = requests.get(
        f'https://wallpaperwaifu.com/page/{pdda}',
        headers=headers,
    ).text
    wb = etree.HTML(response)
    html = wb.xpath('//*[@id="main-content"]/div/div[1]/article')
    if len(html) == 0:
        print("所有数据已获取完毕")
        break
    else:
        mk_create()
        ci = 1
        for li in html:
            a = li.xpath('./div/div[1]/div/a/img/@data-srcset')
            if len(a) != 0:
                image = a[0].split(',')
                if len(image)-1 < 3:
                    image = image[2].replace('1500w','').replace(' ','')
                else:
                    image = image[3].replace('1920w','').replace(' ','')
                print(image,'\n')
                imagec = requests.get(url=image)
                with open(f'{mk_create()}/{ci}.jpg',mode='wb')as f:
                    f.write(imagec.content)
                    ci +=1
                time.sleep(0.3)
        print("第%d页获取完毕==================" % pdda,end='\n')
        pdda+=1