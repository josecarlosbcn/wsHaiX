from websites.mediabiasfactcheck.home import Home
from websites.mediabiasfactcheck.level_one_page import LevelOnePage
from websites.mediabiasfactcheck.level_two_page import LevelTwoPage
from websites.mediabiasfactcheck.excel.excel import MediaBiasFatchcheckEXCEL
from constants import URL
import time


class WebScrapping:
    def __init__(self, url):
        home = Home(url)
        excel = MediaBiasFatchcheckEXCEL(URL.EXCEL_FILE)
        rows = 1
        print("START OF PROCESS!!!")
        for k, v in home.menu.items():
            print(f"\nProcessing {k} bias websites")
            pagel1 = LevelOnePage(v)
            for k1, v1 in pagel1.websites.items():
                print(f"--- Processing of content of page: {v1}")
                time.sleep(1)
                print(f"--- Request time: {time.ctime()}")
                pagel2 = LevelTwoPage(v1)
                params = {"row": rows, "media" : v1, "type": pagel2.get_factual_reporting(), "bias" : k}
                excel.write_row(params)
                print(f"--- End of processing of content of page: {v1}")
                rows += 1
            print(f"End of processing {k} bias websites")
        print("\nEND OF PROCESS!!!")
