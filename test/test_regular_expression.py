import unittest
import re
from websites.mediabiasfactcheck.level_two_page import LevelTwoPage


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     txt = "<strong>MOSTLY FACTUAL</strong>"
    #     result = re.search("MOSTLY FACTUAL", txt)
    #     print(result)
        #self.assertEqual(True, result)

    def test_level_page_two(self):
        pagel2 = LevelTwoPage("https://mediabiasfactcheck.com/committee-constructive-tomorrow-cfact-org/")
        print(pagel2.get_factual_reporting())


if __name__ == '__main__':
    unittest.main()
