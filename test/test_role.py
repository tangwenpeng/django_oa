from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.timeout = 60
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def tearDown(self):
        pass

    # self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8080/app/index/')

        self.assertIn('OA', self.browser.title)
        # 组织管理
        login_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="navBar"]/ul/li[2]/a')))
        login_link.click()
        # 岗位管理
        login_link1 = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="navBar"]/ul/li[2]/dl/dd[2]/a')))
        login_link1.click()

        # 跳转iframe
        self.browser.switch_to.frame(1)
        # 点击添加岗位
        login_link_2 = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/form/blockquote/div[2]/a')))
        login_link_2.click()

        # 跳转iframe
        self.browser.switch_to.frame(0)
        # 输入岗位名
        name_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form/div[1]/div[1]/div/input')))
        name_input.clear()
        name_input.send_keys('酱油员工')

        # 输入岗位编号
        no_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/form/div[1]/div[2]/div/input')))
        no_input.clear()
        no_input.send_keys('JY')

        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div/button[1]')))
        submit_button.click()

        # name_span = self.wait.until(
        #     EC.presence_of_element_located((By.XPATH, '')))
        # self.assertEqual(name_span.text, '酱油员工')

    # user_login_link = self.browser.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn')
    # user_login_link.click()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
