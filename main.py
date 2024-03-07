from selenium import webdriver
import unittest
import unittestreport
class TestBaidu(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.get('https://www.baidu.com')

    def test_01(self):
        '''执行用例1'''
        print('001')

    def test_01(self):
        '''执行用例2'''
        print('002')

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main':
    unittest.main()