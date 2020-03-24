import re
import requests
from time import time

def infoGet(url):
    try:
        r = requests.get(url, timeout = 30)
        r.encoding = ('utf-8')
        r.raise_for_status
        return r.text
    except:
        return ''

def infoParser(av, info):
    try:
        pattern = r'"aid":{0},"bvid":"\w+"'.format(av)
        bv = re.search(pattern,info)
        if bv:
            bv = eval(bv.group().split(':')[2])
            return bv
    except:
        return ''

def infoPrint(av, bv, n, format_):
    print(format_.format(av,bv))
    with open(f'AV-BV(最高至AV{n}).txt','a') as f:
        f.write(format_.format(av,bv))
        f.write('\n')

def main():
    n = int(input('要爬取的最大AV号：'))
    startTime = time()
    format_ = '{0:<20}\t{1:<20}'
    with open (f'AV-BV(最高至AV{n}).txt','a') as f:
        f.write(format_.format('AV号','BV号'))
        f.write('\n')
    print(format_.format('AV号', 'BV号'))
    for i in range(1,n+1):
        url = f'https://api.bilibili.com/x/web-interface/search/all/v2?keyword=av{i}'
        try:
            html = infoGet(url)
            bv = infoParser(i,html)
            infoPrint(i, bv, n, format_)
        except:
            continue
    endTime = time()
    alltime = round(endTime-startTime,2)
    print(f'本次用时{alltime}s')
    input('按下回车以退出')
main()
