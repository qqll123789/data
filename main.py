from selenium import webdriver
import unittest
import unittestreport
from BeautifulReport import BeautifulReport
import unittestreport
class TestBaidu(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_01(self):
        u'''执行用例1'''
        self.driver.get('https://www.baidu.com')
        self.assertEqual(1,2)
        print('001')

    def test_02(self):
        u'''执行用例2'''
        self.driver.get('https://www.baidu.com')
        print('002')

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestBaidu('test_01'))
    suit.addTest(TestBaidu('test_02'))

    #BeautifulReport(suit).report(filename='1',description='测试报告',)
    unittestreport.TestRunner(suit,filename="report.html",
                 report_dir=".",
                 title=u'测试报告',
                 tester='qiao',
                 desc=u"自动化项目测试生成的报告",
                 templates=1).run()

