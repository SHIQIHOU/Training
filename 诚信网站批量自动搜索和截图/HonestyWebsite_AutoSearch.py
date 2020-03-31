from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys

source = pd.read_excel('公司列表.xlsx', sheet_name=[0], header=0)
company_name=source[0]
chrome_driver = 'F:/Python/Scripts/chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_driver)

for x in company_name.iloc[:,0]:
    browser.get("https://sichuan.chinatax.gov.cn/jsearchfront/search.do?websiteid=510000000000000&searchid=12&pg=&p=1&tpl=3&q=&pq=&oq=&eq=&pos=&begin=&end=")
    browser.maximize_window()
    time.sleep(1)
    className1 = browser.find_element_by_id("q")
    className1.send_keys(x)
    className1.send_keys(Keys.ENTER)
    #className2 = browser.find_element_by_id("query_btn")
    #className2.click()
    filename=x +'.png'
    try:
        browser.switch_to_window(browser.window_handles[-1])
        '''
        target = browser.find_element_by_xpath("//div[@class='crumbsNav']")
        browser.execute_script("arguments[0].scrollIntoView();", target)
        '''
        time.sleep(1)
        pic_url=browser.get_screenshot_as_file(filename)
    except BaseException as msg:
        print(msg)
browser.quit()
