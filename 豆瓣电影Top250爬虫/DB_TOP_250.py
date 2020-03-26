import requests
import bs4

def open_url(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
                  ,  'Cookie' : '_atrk_siteuid=FaOYzau_9726TAUx; id=22432df695b2002e||t=1547692282|et=730|cs=002213fd4805629f4e5a05e6b7'
               }
    res = requests.get(url, headers=headers)
    return res

def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    #电影名称
    movies = []
    targets = soup.find_all("div", class_="hd")
    for each in targets:
        movies.append(each.a.span.text)
    #评分
    ranks = []
    targets = soup.find_all("span", class_="rating_num")
    for each in targets:
        ranks.append("  评分：%s " % each.text)
    #简介
    introductions = []
    targets = soup.find_all("div", class_="bd")
    for each in targets:
        try:
            introductions.append(each.p.text.split('\n')[1].strip() + each.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(movies)
    for i in range(length):
        result.append(movies[i] + ranks[i] + introductions[i] + '\n')
    return result
    
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    depth = soup.find("span", class_="next").previous_sibling.previous_sibling.text
    return int(depth)

def main():
    host = "https://movie.douban.com/top250"
    res = open_url(host)
    depth = find_depth(res)

    result = []
    for i in range(depth):
        url = host + '/?start=' + str(25 * i)
        res = open_url(url)
        result.extend(find_movies(res))

    with open("豆瓣电影Top250.txt", "w", encoding="utf-8") as f:
        for each in result:
            f.write(each)

if __name__ == "__main__":
    main()
