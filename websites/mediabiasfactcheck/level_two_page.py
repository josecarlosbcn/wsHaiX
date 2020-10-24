from com.bs4.document.document import Document
import re
from constants import FACTUAL_REPORTING

class LevelTwoPage:
    def __init__(self, url):
        self.doc = Document(url)
        #print(self.doc.soup.prettify())

    def __detect_tag_h3(self):
        '''
        :return: A dictionary with the result of the search and if any one of the types has been found
        '''
        soup = self.doc.soup
        result = {}
        try:
            tag = soup.find_all("h3", attrs={"style": "text-align: center;"})[0].find_next("p")
            if tag is not None:
                result["mf"] = True if re.search(FACTUAL_REPORTING.MOSTLY_FACTUAL, str(tag.prettify())) is not None else False
                result["mx"] = True if re.search(FACTUAL_REPORTING.MIXED, str(tag.prettify())) is not None else False
                result["hg"] = True if re.search(FACTUAL_REPORTING.HIGH, str(tag.prettify())) is not None else False
                result["lw"] = True if re.search(FACTUAL_REPORTING.LOW, str(tag.prettify())) is not None else False
                result["vl"] = True if re.search(FACTUAL_REPORTING.VERY_LOW, str(tag.prettify())) is not None else False
                result["vh"] = True if re.search(FACTUAL_REPORTING.VERY_HIGH, str(tag.prettify())) is not None else False
                result["found"] = True if result["mf"] or result["mx"] or result["hg"] or result["lw"] or result["vl"] or result["vh"] else False
        except IndexError:
            result["found"] = False
        return result

    def __detect_tag_div(self):
        '''
        :return: A dictionary with the result of the search and if any one of the types has been found
        '''
        soup = self.doc.soup
        result = {}
        tags = soup.find_all("div", class_="entry-content")
        if len(tags) > 0:
            for  t in tags:
                result["mf"] = True if re.search(FACTUAL_REPORTING.MOSTLY_FACTUAL, str(t.prettify())) is not None else False
                result["mx"] = True if re.search(FACTUAL_REPORTING.MIXED, str(t.prettify())) is not None else False
                result["hg"] = True if re.search(FACTUAL_REPORTING.HIGH, str(t.prettify())) is not None else False
                result["lw"] = True if re.search(FACTUAL_REPORTING.LOW, str(t.prettify())) is not None else False
                result["vl"] = True if re.search(FACTUAL_REPORTING.VERY_LOW, str(t.prettify())) is not None else False
                result["vh"] = True if re.search(FACTUAL_REPORTING.VERY_HIGH, str(t.prettify())) is not None else False
                result["found"] = True if result["mf"] or result["mx"] or result["hg"] or result["lw"] or result["vl"] or result["vh"] else False
                if result["found"]:
                    break
        else:
            result["found"] = False
        return result

    def __detect_tag_div2(self):
        '''
        :return: A dictionary with the result of the search and if any one of the types has been found
        '''
        soup = self.doc.soup
        result = {}
        tags = soup.find_all("div", class_="entry clearfix")
        if len(tags) > 0:
            for  t in tags:
                result["mf"] = True if re.search(FACTUAL_REPORTING.MOSTLY_FACTUAL, str(t.prettify())) is not None else False
                result["mx"] = True if re.search(FACTUAL_REPORTING.MIXED, str(t.prettify())) is not None else False
                result["hg"] = True if re.search(FACTUAL_REPORTING.HIGH, str(t.prettify())) is not None else False
                result["lw"] = True if re.search(FACTUAL_REPORTING.LOW, str(t.prettify())) is not None else False
                result["vl"] = True if re.search(FACTUAL_REPORTING.VERY_LOW, str(t.prettify())) is not None else False
                result["vh"] = True if re.search(FACTUAL_REPORTING.VERY_HIGH, str(t.prettify())) is not None else False
                result["found"] = True if result["mf"] or result["mx"] or result["hg"] or result["lw"] or result["vl"] or result["vh"] else False
                if result["found"]:
                    break
        return result

    def get_factual_reporting(self):
        '''
            :return: A string with the value of Factual Reporting
        '''
        if self.doc.soup is not None:
            result = self.__detect_tag_h3()
            if not result["found"]:
                result = self.__detect_tag_div()
                if not result["found"]:
                    result = self.__detect_tag_div2()
            if result["mf"]:
                txt = FACTUAL_REPORTING.MOSTLY_FACTUAL
            if result["mx"]:
                txt = FACTUAL_REPORTING.MIXED
            if result["hg"]:
                txt = FACTUAL_REPORTING.HIGH
            if result["lw"]:
                txt = FACTUAL_REPORTING.LOW
            if result["vl"]:
                txt = FACTUAL_REPORTING.VERY_LOW
            if result["vh"]:
                txt = FACTUAL_REPORTING.VERY_HIGH
            if not result["found"]:
                txt = "NOT FOUND!!!"
        else:
            txt = "PAGE NOT FOUND!!!"
        return txt
