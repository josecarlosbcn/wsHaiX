from bs4 import BeautifulSoup
import urllib.request, urllib.error


class Document:
    def __init__(self, url):
        self.soup = Document.__get_document(url)

    '''Methods'''
    @staticmethod
    def __get_document(url):
        '''
            :param url: url to the site where we want to retrieve information
            :return: soup with all the content of the data. Otherwise, the program will exit
        '''
        req = urllib.request.Request(url)
        try:
            page = urllib.request.urlopen(req)
            html = page.read()
            soup = BeautifulSoup(html, "html.parser")
            return soup
        except urllib.error.URLError as ex:
            print(f"url: {url} \n reason: {ex.reason}")
            return None
