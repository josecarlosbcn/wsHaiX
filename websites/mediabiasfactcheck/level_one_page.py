from com.bs4.document.document import Document


class LevelOnePage:
    def __init__(self, url):
        self.doc = Document(url)
        self.websites = self.__get_list_websites()

    def __get_list_websites(self):
        '''
            :return: Returns a dictionary with like key the name of source and value the url to access to the page of its content
        '''
        soup = self.doc.soup
        table = soup.find("table", class_= "sort")
        list = table.find_all("a")
        result = {}
        for item in list:
            result[item.string] = item["href"]
        return result
