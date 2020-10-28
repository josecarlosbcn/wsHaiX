from com.bs4.document.document import Document
import re
from constants import FACTUAL_REPORTING


class LevelTwoPage:
    def __init__(self, url):
        self.doc = Document(url)
        #print(self.doc.soup.prettify())

    # def __detect_tag_h3(self):
    #     '''
    #     :return: A dictionary with the result of the search and if any one of the types has been found
    #     '''
    #     soup = self.doc.soup
    #     result = {}
    #     try:
    #         tag = soup.find_all("h3", attrs={"style": "text-align: center;"})[0].find_next("p")
    #         if tag is not None:
    #             result["mf"] = True if re.search(FACTUAL_REPORTING.MOSTLY_FACTUAL, str(tag.prettify())) is not None else False
    #             result["mx"] = True if re.search(FACTUAL_REPORTING.MIXED, str(tag.prettify())) is not None else False
    #             result["hg"] = True if re.search(FACTUAL_REPORTING.HIGH, str(tag.prettify())) is not None else False
    #             result["lw"] = True if re.search(FACTUAL_REPORTING.LOW, str(tag.prettify())) is not None else False
    #             result["vl"] = True if re.search(FACTUAL_REPORTING.VERY_LOW, str(tag.prettify())) is not None else False
    #             result["vh"] = True if re.search(FACTUAL_REPORTING.VERY_HIGH, str(tag.prettify())) is not None else False
    #             result["found"] = True if result["mf"] or result["mx"] or result["hg"] or result["lw"] or result["vl"] or result["vh"] else False
    #     except IndexError:
    #         result["found"] = False
    #     return result
    #
    # def __detect_tag_div(self):
    #     '''
    #     :return: A dictionary with the result of the search and if any one of the types has been found
    #     '''
    #     soup = self.doc.soup
    #     result = {}
    #     tags = soup.find_all("div", class_="entry-content")
    #     if len(tags) > 0:
    #         for  t in tags:
    #             result["mf"] = True if re.search(FACTUAL_REPORTING.MOSTLY_FACTUAL, str(t.prettify())) is not None else False
    #             result["mx"] = True if re.search(FACTUAL_REPORTING.MIXED, str(t.prettify())) is not None else False
    #             result["hg"] = True if re.search(FACTUAL_REPORTING.HIGH, str(t.prettify())) is not None else False
    #             result["lw"] = True if re.search(FACTUAL_REPORTING.LOW, str(t.prettify())) is not None else False
    #             result["vl"] = True if re.search(FACTUAL_REPORTING.VERY_LOW, str(t.prettify())) is not None else False
    #             result["vh"] = True if re.search(FACTUAL_REPORTING.VERY_HIGH, str(t.prettify())) is not None else False
    #             result["found"] = True if result["mf"] or result["mx"] or result["hg"] or result["lw"] or result["vl"] or result["vh"] else False
    #             if result["found"]:
    #                 break
    #     else:
    #         result["found"] = False
    #     return result
    #
    # def __detect_tag_div2(self):
    #     '''
    #     :return: A dictionary with the result of the search and if any one of the types has been found
    #     '''
    #     soup = self.doc.soup
    #     result = {}
    #     tags = soup.find_all("div", class_="entry clearfix")
    #     if len(tags) > 0:
    #         for  t in tags:
    #             result["mf"] = True if re.search(FACTUAL_REPORTING.MOSTLY_FACTUAL, str(t.prettify())) is not None else False
    #             result["mx"] = True if re.search(FACTUAL_REPORTING.MIXED, str(t.prettify())) is not None else False
    #             result["hg"] = True if re.search(FACTUAL_REPORTING.HIGH, str(t.prettify())) is not None else False
    #             result["lw"] = True if re.search(FACTUAL_REPORTING.LOW, str(t.prettify())) is not None else False
    #             result["vl"] = True if re.search(FACTUAL_REPORTING.VERY_LOW, str(t.prettify())) is not None else False
    #             result["vh"] = True if re.search(FACTUAL_REPORTING.VERY_HIGH, str(t.prettify())) is not None else False
    #             result["found"] = True if result["mf"] or result["mx"] or result["hg"] or result["lw"] or result["vl"] or result["vh"] else False
    #             if result["found"]:
    #                 break
    #     return result
    #
    # def __detect_tag_image(self):
    #     soup = self.doc.soup
    #     result = {}
    #     tags = soup.find("div", class_="entry clearfix").h2.find_all("img")[1]
    #     fr = tags["data-image-title"][4:].upper()
    #     result["mf"] = True if FACTUAL_REPORTING.MOSTLY_FACTUAL == fr else False
    #     result["mx"] = True if FACTUAL_REPORTING.MIXED == fr else False
    #     result["hg"] = True if FACTUAL_REPORTING.HIGH == fr else False
    #     result["lw"] = True if FACTUAL_REPORTING.LOW == fr else False
    #     result["vl"] = True if FACTUAL_REPORTING.VERY_LOW == fr else False
    #     result["vh"] = True if FACTUAL_REPORTING.VERY_HIGH == fr else False
    #     result["found"] = True if result["mf"] or result["mx"] or result["hg"] or result["lw"] or result["vl"] or result["vh"] else False
    #     return result

    def __detect_tag_image(self):
        soup = self.doc.soup
        result = {}
        result["mf"] = True if re.search('(\"MBFCMostlyFactual\")', str(soup), re.IGNORECASE) or \
                               re.search('(\"mbfc_mostly_factual\")', str(soup), re.IGNORECASE) or \
                               re.search('(\"MostlyFactual\")', str(soup), re.IGNORECASE) or \
                               re.search('<strong>MOSTLY\s*FACTUAL<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('strong>MOSTLY\s*FACTUAL<br\s*\/>\n<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<strong><span style=\"color: #008000;\">MOSTLY\s*FACTUAL<\/span><br\s*\/>\n<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<span style=\"color: #808000;\">MOSTLY\s*FACTUAL<\/span>', str(soup), re.IGNORECASE) else False
        result["mx"] = True if re.search('(\"MBFCMixed\")', str(soup), re.IGNORECASE)  or \
                               re.search('(\"mbfc_mixed\")', str(soup), re.IGNORECASE) or \
                               re.search('(\"MixedFactual\")', str(soup), re.IGNORECASE) or \
                               re.search('<strong>MIXED<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('strong>MIXED<br\s*\/>\n<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<strong><span style=\"color: #ff6600;\">MIXED<\/span><br\s*\/>\n<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<span style=\"color:\s*#ff6600;\"><b>MIXED<\/b><\/span><\/p>', str(soup), re.IGNORECASE) or \
                               re.search('<strong><span style=\"color:\s*#ff6600;\">MIXED<br\s*\/>\n<\/span><\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<span style=\"color:\s*#ff6600;\"><strong>\s*MIXED<br\s*\/>\n<\/strong><\/span>', str(soup), re.IGNORECASE) or \
                               re.search('<span style=\"color: #008000;\"><strong><span style=\"color: #ff6600;\">\s*MIXED<\/span><br\s*\/>\n<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<span style=\"color:\s*#ff6600;\"><strong>\s*MIXED<\/strong><\/span>', str(soup), re.IGNORECASE) or \
                               re.search('<span style=\"color: #ff6600;\">', str(soup), re.IGNORECASE)  else False
        result["hg"] = True if re.search('(\"MBFCHigh\")', str(soup), re.IGNORECASE) or \
                               re.search('(\"mbfc_high\")', str(soup), re.IGNORECASE) or \
                               re.search('(\"HighFactual\")', str(soup), re.IGNORECASE) or \
                               re.search('<strong>HIGH<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('strong>HIGH<br\s*\/>\n<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<strong><span style=\"color: #008000;\">HIGH<\/span><br\s*\/>\n<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<strong><span style=\"color: #008000;\">HIGH<br\s*\/>\n<\/span><\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<strong><span style=\"color: #008000;\">HIGH<br>\n<\/span><\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<span style=\"color: #008000;\"><strong>HI<\/strong><strong>GH<br\s*\/>\n<\/strong><\/span>', str(soup), re.IGNORECASE) or \
                               re.search('<span style=\"color: #008000;\">HIGH<\/span>', str(soup), re.IGNORECASE) or \
                               len(soup.select("span[data-iceapw='1']")) > 0 else False
        result["lw"] = True if re.search('(\"MBFCLow\")', str(soup), re.IGNORECASE) or \
                               re.search('(\"mbfc_low\")', str(soup), re.IGNORECASE) or \
                               re.search('(\"LowFactual\")', str(soup), re.IGNORECASE) or \
                               re.search('<strong>LOW<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('strong>LOW<br\s*\/>\n<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<strong><span style=\"color: #008000;\">LOW<\/span><br\s*\/>\n<\/strong>', str(soup), re.IGNORECASE) else False
        result["vl"] = True if re.search('(\"MBFCVeryLow\")', str(soup), re.IGNORECASE) or \
                               re.search('(\"mbfc_very_low\")', str(soup), re.IGNORECASE) or \
                               re.search('<strong>VERY\s*LOW<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('strong>VERY\s*LOW<br\s*\/>\n<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<strong><span style=\"color: #008000;\">VERY\s*LOW<\/span><br\s*\/>\n<\/strong>', str(soup), re.IGNORECASE) else False
        result["vh"] = True if re.search('(\"MBFCVeryhigh\")', str(soup), re.IGNORECASE) or \
                               re.search('(\"mbfc_very_high")', str(soup), re.IGNORECASE) or \
                               re.search('<strong>VERY\s*HIGH<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('strong>VERY\s*HIGH<br\s*\/>\n<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<strong><span style=\"color: #008000;\">VERY\s*HIGH<\/span><br\s*\/>\n<\/strong>', str(soup), re.IGNORECASE) or \
                               re.search('<span style=\"color: #008000;\"><strong>VERY-HIGH<\/strong><\/span>', str(soup), re.IGNORECASE) else False
        result["found"] = True if result["mf"] or result["mx"] or result["hg"] or result["lw"] or result["vl"] or result["vh"] else False
        return result

    def get_factual_reporting(self):
        '''
            :return: A string with the value of Factual Reporting
        '''
        if self.doc.soup is not None:
            result = self.__detect_tag_image()
            # result = self.__detect_tag_h3()
            # if not result["found"]:
            #     result = self.__detect_tag_div()
            #     if not result["found"]:
            #         result = self.__detect_tag_div2()
            #         if not result["found"]:
            #             result = self.__detect_tag_image()
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
