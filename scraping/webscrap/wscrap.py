from urllib.request import urlopen

from bs4 import BeautifulSoup
import itertools

url_aj = "https://www.rsssearchhub.com/feed/ca2d2ce8cde6dafe80124164e7db72f7/"
filepath = "html/aj.html"


class NewsScraper:
    __url  =''
    __data =''
    __wlog = None
    __soup = None


    def __init__(self, url, wlog):
        self.__url  = url
        self.__wlog = wlog

    def retrive_webpage(self):
        try:
            html = urlopen(self.__url)
        except Exception as e:
            print(e)
            self.__wlog.report(e)
        else:
            self.__data = html.read()
            if len(self.__data) > 0:
                print("Retrived Successfully")

    def read_webpage_from_html(self, filepath=filepath):
        try:
            with open(filepath) as fobj:
                self.__data = fobj.read()
        except Exception as e:
            print(e)
            self.__wlog.report(e)
 
    def write_webpage_as_html(self, filepath=filepath, data=''):
       
        try:
            with open(filepath, 'wb') as fobj:
                if data:
                    fobj.write(data)
                else:
                    fobj.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog.report(e)


    def change_url(self, url):
        self.__url = url

    def print_data(self):
        print(self.__data)

    def convert_data_to_bs4(self):
        self.__soup  = BeautifulSoup(self.__data, "html.parser")

    def parse_soup_to_simple_html(self):
        # news_list = self.__soup.select('h3 a')
        news_list = self.__soup.find_all("a", attrs={"class": "card"})
        news_title_list = self.__soup.select('article h3')

        htmltext = """
        <html>
        <head><title>Simple news link Scrapper</title></head>
        <body>
        {NEWS_LINKS}
        </body>
        </html>
        """

        
        news_links = '<ol>'
        news_lists = []
        for tag, tit in itertools.zip_longest(news_list, news_title_list):
            if tag.get('href'):
                link = tag.get('href')
                title = tit.string
                news_lists.append({"title":title, "link":link})
                # if 'dailysangram.info/post' in link:
                #     news_lists.append({"title":title, "link":link})
                news_links += "<li><a href='{}'target='_blank'>{}</li>\n".format(link, title)

        news_links +='</ol>'

        htmltext = htmltext.format(NEWS_LINKS=news_links)
        # import pdb; pdb.set_trace()
        print("hello world")
        self.write_webpage_as_html( filepath='html/simplenews.html', data=htmltext.encode())
        return news_lists