from selenium import webdriver
import unittest
import unittestreport
class TestBaidu(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_01(self):
        '''执行用例1'''
        self.driver.get('https://www.baidu.com')
        print('001')

    def test_01(self):
        '''执行用例2'''
        self.driver.get('https://www.baidu.com')
        print('002')

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()