# http://img4.imgtn.bdimg.com/it/u=1888370504,2362661588&fm=26&gp=0.jpg
#
#
# http://img3.imgtn.bdimg.com/it/u=3059596510,1572191085&fm=26&gp=0.jpg
# http://img1.imgtn.bdimg.com/it/u=3173584241,3533290860&fm=26&gp=0.jpg
# 用gevent 下载上述两个图片

import urllib.request
import gevent
from gevent import monkey


monkey.patch_all()

def down_imgs(name,ur):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
               'Referer':'',}

    red1 = urllib.request.Request(url =ur,headers = headers)
    red = urllib.request.urlopen(red1).read()

    with open(name, 'wb') as f:
        f.write(red)

def main():
    gevent.joinall([
        gevent.spawn(down_imgs,'1.jpg','http://img4.imgtn.bdimg.com/it/u=1888370504,2362661588&fm=26&gp=0.jpg'),
        gevent.spawn(down_imgs,'2.jpg','http://img3.imgtn.bdimg.com/it/u=3059596510,1572191085&fm=26&gp=0.jpg'),
        gevent.spawn(down_imgs,'3.jpg','http://img1.imgtn.bdimg.com/it/u=3173584241,3533290860&fm=26&gp=0.jpg'),
    ])

if __name__ == '__main__':
    main()

