import requests
import json
import bs4

def get_url(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
                  ,  'Cookie' : 'BIDUPSID=823DE7F35A0D5848C40A7F9CF8F834B1', 
               'referer' : 'https://y.qq.com/n/yqq/song/001QJyJ32zybEe.html'}
    res = requests.get(url, headers = headers)
    return res

def main():
    url1 = input("请输入需要查询的歌曲网页链接: ")
    res1 = get_url(url1)
    soup = bs4.BeautifulSoup(res1.text, "html.parser")
    content = soup.find("a", class_="mod_btn js_more")
    songid = int(content['data-id'])
    url2 = "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid={}&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010".format(songid)
    res2 = get_url(url2)
    comments = json.loads(res2.text)
    hot_comments = comments['hot_comment']['commentlist']
    with open('test.txt', 'w', encoding='utf-8') as file:
        for each in hot_comments:
            file.write(each['nick'] + ' : ' + '\n' + each['rootcommentcontent'] + '\n')
            file.write('-----------------------------------------------\n')
    
    
if __name__ =="__main__":
    main()
