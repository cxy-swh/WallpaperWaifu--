import os
import time


def hecheng():
    def mk():
        mks = './WallpaperWaifu爬虫数据'
        if not os.path.exists(f'{mks}/全部图片'):
            os.makedirs(f'{mks}/全部图片')
        return mks
    name = len(os.listdir(mk() + '/图片'))
    yy = 1
    for i in range(1,name+1):
        name2 = mk() + f'/图片/第{i}页'
        print(f'正在获取第{i}页',end='\n')
        for h in range(1,len(os.listdir(name2))+1):
            xxxx = mk().replace('./','')
            os.system(f'copy {xxxx}\\图片\\第{i}页\\{h}.jpg {xxxx}\\全部图片\\{yy}.jpg')
            print(yy)
            time.sleep(0.3)
            yy += 1
hecheng()