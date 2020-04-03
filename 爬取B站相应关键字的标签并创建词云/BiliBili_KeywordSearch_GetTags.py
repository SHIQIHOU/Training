import requests
import bs4

def getTags(res, page):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    result = ""

    #获得网址
    links = []
    targets = soup.find_all("div", class_='headline clearfix')
    for each in targets:
        links.append('https:' + each.a['href'])

    #逐个获取标签
    tags = []
    for each in links:
        res1 = requests.get(each)
        soup1 = bs4.BeautifulSoup(res1.text, 'html.parser')
        targets = soup1.find_all("li", class_="tag")
        for one in targets:
            result += one.a.text + ' '

    return result

def main():
    searchname = input('请输入你要搜索的内容：')
    pagenum = input('请输入你要搜索的页数：')
    final_result = ""
    for i in range(int(pagenum)):
        url = "https://search.bilibili.com/all?keyword=" + searchname + "&from_source=nav_suggest_new&order=click&duration=0&tids_1=0&page=" + str(i + 1)
        res = requests.get(url)
        final_result += getTags(res, i)
    with open('test.txt', 'w', encoding='utf-8') as file:
        file.write(final_result)

if __name__ == "__main__":
    main()
