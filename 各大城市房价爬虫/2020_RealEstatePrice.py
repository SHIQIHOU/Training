import requests
import bs4
import re
import openpyxl

def open_url(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
                  ,  'Cookie' : '_atrk_siteuid=FaOYzau_9726TAUx; id=22432df695b2002e||t=1547692282|et=730|cs=002213fd4805629f4e5a05e6b7'
               }
    res = requests.get(url, headers=headers)
    return res

def find_data(res):
    data = []
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    target = soup.find_all("li", class_="clearfix up")
    for each in target:
        data.append([
            re.search(r'(..)房价', each.a.b.text).group(1),
            each.a.span.text,
            each.a.em.text])
    return data

def to_excel(data):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws = wb.active
    ws.append(['城市', '房价', '涨跌幅'])
    for each in data:
        ws.append(each)
    wb.save("2020年全国城市房价排行榜.xlsx")
    
def main():
    url = "https://www.anjuke.com/fangjia/quanguo2020/"
    res = open_url(url)
    data = find_data(res)
    to_excel(data)

if __name__=="__main__":
    main()
