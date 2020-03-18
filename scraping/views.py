from django.shortcuts import render
from .webscrap import wlog
from .webscrap import wscrap


# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------------
#      Execute JavaScript
# --------------------------

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
import time
import sys
import os
import itertools
 

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1024x1400")
    # import pdb; pdb.set_trace()
    # download Chrome Webdriver  
    # https://sites.google.com/a/chromium.org/chromedriver/download
    # put driver executable file in the script directory
    # import pdb; pdb.set_trace()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    chrome_driver = os.path.join(BASE_DIR, "chromedriver")
    # chrome_driver = "jh\johukum\scraping\chromedriver.exe"

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

    # driver.get("https://github.com")
    driver.get("https://www.prothomalo.com")
    # assert "GitHub".lower() in driver.title.lower()
    
    # scrap info
    # h1_elem=driver.find_elements_by_class_name("title")
    a_elem = driver.find_elements_by_css_selector('div a.link_overlay')
    title_elem = driver.find_elements_by_css_selector('div h2 span.title')
    # h2_elem = driver.find_elements_by_css_selector('span.title')
    # h1_elem = driver.find_element_by_tag_name("h2")
    # print(h1_elem.text)
    # print(h1_elem)
    news = []
    for link, titl in itertools.zip_longest(a_elem, title_elem):
        # quoteArr = quote.get_attribute("href")
        # news.append(quoteArr)
        link_elem = link.get_attribute("href")
        # link_href = link_elem.get_attribute("href")
        title =titl.text
        news.append({"title":title, "link":link_elem})
        print()

    return news
 
    # fill and submit form
    # elem = driver.find_element_by_name("q")
    # elem.clear()
    # elem.send_keys("python")
    # elem.send_keys(Keys.RETURN)

    # screenshot capture
    # driver.get_screenshot_as_file("python-github.png")
    # driver.close()

# if __name__ == '__main__' : main()



# Create your views here.


def hello(request):
    # wlog.set_custom_log_info('html/error.log')

    # news_scrap = wscrap.NewsScraper(wscrap.url_aj, wlog)
    # news_scrap.retrive_webpage()
    # news_scrap.write_webpage_as_html()

    # news_scrap.read_webpage_from_html()
    # news_scrap.convert_data_to_bs4()
    # news_scrap.print_data()
    # data=news_scrap.parse_soup_to_simple_html()
    # print(data)
    data = main()
    context={'data':data, 'news_paper' : 'Prothon-Alo'}
    return render(request, 'hello.html', context)


# def hello(request):

#     def main():
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--window-size=1024x1400")

#         # download Chrome Webdriver  
#         # https://sites.google.com/a/chromium.org/chromedriver/download
#         # put driver executable file in the script directory
#         # import pdb; pdb.set_trace()
#         # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         chrome_driver = os.path.join(os.getcwd(), "chromedriver.exe")

#         driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

#         # driver.get("https://github.com")
#         driver.get("https://www.prothomalo.com")
#         assert "GitHub".lower() in driver.title.lower()
    
#         # scrap info
#         h1_elem = driver.find_element_by_tag_name("h2")
#         # print(h1_elem.text)
#         print(h1_elem)

#         # fill and submit form
#         # elem = driver.find_element_by_name("q")
#         # elem.clear()
#         # elem.send_keys("python")
#         # elem.send_keys(Keys.RETURN)

#         # screenshot capture
#         # driver.get_screenshot_as_file("python-github.png")
#         # driver.close()

#     if __name__ == '__main__' : main()
    
    
#     return render(request, 'hello.html', context)



# #imports
# from .models import Road
# from bs4 import BeautifulSoup
# import pandas as pd
# import requests

# url='http://camden.gov.uk/ccm/navigation/transport-and-streets/parking/parking-bay-suspensions/search-for-parking-bay-suspensions/'
# r = requests.get(url)
# html_doc = r.text
# soup = BeautifulSoup(html_doc,"html.parser")
# table = soup.find('table')
# rows = table.find_all('tr')
# pd.set_option('display.max_colwidth', -1)
# df = pd.read_html(str(table))[0]
# df['href'] = [tag['href'] for tag in table.find_all('a')]

# #Delete objects in Django 
# Road.objects.all().delete()

# for zone_index, zone_row in df.iterrows():
#     print(zone_row[0],zone_row[1],zone_row[2])
#     url=zone_row[2]
#     r = requests.get(url)
#     html_doc = r.text
#     soup = BeautifulSoup(html_doc,"html.parser")
#     table = soup.find('table')
#     df2 = pd.read_html(str(table),header=0)[0]
#     df2['href'] = [tag['href'] for tag in table.find_all('a')]
#     road_list = [[zone_row[0],zone_row[1],road_row[0],'Camden','http://registers.camden.gov.uk/SuspendedBays/'+road_row['href'].replace(' ','%20')] 
#                  for road_index,road_row in df2.iterrows() if pd.notnull(road_row[1]) == False ]
#     road_df = pd.DataFrame(road_list,columns=['zone_code','zone','road','borough','suspension_href'])
#     Roads = road_df.to_dict('roads')
#     model_instances = [Road(
#         road=record['road'],
#         zone_code=record['zone_code'],
#         borough=record['borough'],
#         zone=record['zone'],
#         suspension_href=record['suspension_href'],
        
        
#     ) for record in Roads]
   
#     Road.objects.bulk_create(model_instances)
    

def main2():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1024x1400")
    # download Chrome Webdriver  
    # https://sites.google.com/a/chromium.org/chromedriver/download
    # put driver executable file in the script directory
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    chrome_driver = os.path.join(BASE_DIR, "chromedriver")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

    driver.get("https://www.kalerkantho.com")
    # email_input = driver.find_element_by_xpath("//form[input/@name='emailId/mobileNo']")
    # import pdb; pdb.set_trace()
    # element = driver.find_element_by_xpath("//div[@id='mCSB_1_container']")
    items = driver.find_elements_by_css_selector('li > a')
    # items = driver.find_elements_by_css_selector('#mCSB_1_container li a')
    
    # elements = element.find_elements_by_tag_name('li > a')
    # elements = element.find_elements_by_css_selector('li > a')
    news = []
    for item in items:
        # import pdb; pdb.set_trace()
        # item_link = item.find_elements_by_css_selector('li > a')
        link_elem = item.get_attribute("href")
        title =item.text
        if len(title) > 15:
            news.append({"title":title, "link":link_elem})
        # if title != []:
            # news.append({"title":title, "link":link_elem})
        print(item)
        
    print(news)
    # import pdb; pdb.set_trace()
    return news
 

def kalerkantho_view(request):
    data = main2()
    context={'data':data,'news_paper' : 'kalerkantho'}
    return render(request, 'hello.html', context)
