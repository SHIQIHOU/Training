import requests
import bs4
import re

def getContent(res, page):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    result = ""

    #标题
    titles = []
    targets = soup.find_all("li", class_='video-item matrix')
    for each in targets:
        titles.append(each.a['title'])

    #网址
    links = []
    targets = soup.find_all("div", class_='headline clearfix')
    for each in targets:
        links.append('https:' + each.a['href'])

    #点击量
    clicks = []
    targets = soup.find_all("i", class_='icon-playtime')
    for each in targets:
        clicks.append(re.search(r'(\d(.*?))\n', str(each.next_sibling)).group(1))
        
    #弹幕量
    dms = []
    targets = soup.find_all("i", class_='icon-subtitle')
    for each in targets:
        dms.append(re.search(r'(\d(.*?))\n', str(each.next_sibling)).group(1))

    #上传时间
    dates = []
    targets = soup.find_all("i", class_='icon-date')
    for each in targets:
        dates.append(re.search(r'(\d(.*?))\n', str(each.next_sibling)).group(1))

    #UP主
    ups = []
    targets = soup.find_all("span", title='up主')
    for each in targets:
        ups.append(each.a.text)

    length = len(titles)
    for i in range(length):
        result += 'No.' + str(page * 20 + i+1) + '\n' \
                      + '标题: ' + titles[i] +'\n' \
                      + '网址: ' + links[i] + '\n' \
                      + '点击量: ' + clicks[i] + '     ' + '弹幕量: ' + dms[i] + '\n' \
                      + '上传时间: ' + dates[i] + '\n' \
                      + 'UP主: ' + ups[i] + '\n' \
                      + '------------------------------------------------\n'
    return result

def main():
    searchname = input('请输入你要搜索的内容：')
    pagenum = input('请输入你要搜索的页数：')
    final_result = ""
    for i in range(int(pagenum)):
        url = "https://search.bilibili.com/all?keyword=" + searchname + "&from_source=nav_suggest_new&order=click&duration=0&tids_1=0&page=" + str(i + 1)
        res = requests.get(url)
        final_result += getContent(res, i)
    with open('test.txt', 'w', encoding='utf-8') as file:
        file.write(final_result)

if __name__ == "__main__":
    main()
