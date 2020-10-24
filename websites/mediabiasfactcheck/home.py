from com.bs4.document.document import Document


class Home:
    def __init__(self, url):
        self.doc = Document(url)
        self.menu = self.__menu()

    def __menu(self):
        '''
            :return: A dictionary with the bias like key and url like value to access to each page of the menu
        '''
        soup = self.doc.soup
        pm = soup.find("ul", id="mega-menu-info_nav")
        list = pm.find_all("a", class_="mega-menu-link")
        result = {}
        valid_menu_options = ["Left", "Left-Center", "Least Biased", "Right-Center", "Right", "Conspirancy-Pseudoscience",
                        "Questionable Sources", "Pro-Science", "Satire"]
        for element in list:
            if element.string is not None and element.string in valid_menu_options:
                result[element.string] = element["href"]
            #print(element.string) # + " " + element["href"])
        return result
