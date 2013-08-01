#-*-coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from selenium.webdriver import ActionChains
class Dingjia(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://192.168.88.183/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_dingjia(self):
        driver = self.driver
        driver.get(self.base_url + "/dbackup")
        time.sleep(3)
        handle = driver.window_handles
        driver.switch_to_frame(0)
        driver.find_element_by_id("serialRadio").click()
        driver.find_element_by_id("trialRadio").click()
        driver.find_element_by_xpath("//div[3]/label").click()
        driver.find_element_by_id("continue").click()
        driver.switch_to_window(handle)
        driver.find_element_by_id("UserNameID").send_keys("admin")
        driver.find_element_by_id("PWID").send_keys("admin")
        driver.find_element_by_id("LoginButton").click()
        alert = self.driver.switch_to_alert()
        time.sleep(3)

#        addFTP(driver,"ftp1831","192.168.88.183","irene","dingjia","183FTP/complicate")
#        alert.accept()
#------------------------------添加存储服务器-------------------------------------
        def addFTP(driver,name,ip,lname,lpasswd,dir):
            action_chains = ActionChains(driver)
            time.sleep(3)
            action_chains.move_to_element(driver.find_element_by_link_text("存储服务器")).perform()
            action_chains.click(driver.find_element_by_link_text("添加存储服务器")).perform()
#            time.sleep(3)
#            driver.find_element_by_id("strFTPNameID").send_keys(name)
#            se = driver.find_element_by_id("protocalSelect")
#            se.find_element_by_xpath("//option[@value='ftp']").click()
#            time.sleep(3)
#            driver.find_element_by_css_selector("input.input").send_keys(ip)
#            driver.find_element_by_id("strFTPLoginNameID").send_keys(lname)
#            driver.find_element_by_id("strFTPLoginPWID").send_keys(lpasswd)
#            driver.find_element_by_id("nPathID").send_keys(dir)
#            driver.find_element_by_id("nRemanentDateNumID").send_keys("1")
#            driver.find_element_by_id("Submit").click()
#            alert = self.driver.switch_to_alert()
#            alert.accept()
#------------------------------添加存储服务器成功--------------------------------
        time.sleep(5)
#------------------------------注册用户------------------------------------------
#        def addUser(name,passwd,confirmpasswd,email,telephone):
#            action_chains.move_to_element(driver.find_element_by_link_text("用户管理")).perform()
#            action_chains.click(driver.find_element_by_link_text("注册用户")).perform()
#            driver.find_element_by_id("username").send_keys(name)
#            driver.find_element_by_id("password").send_keys(passwd)
#            driver.find_element_by_id("confirmpassword").send_keys(confirmpasswd)
#            driver.find_element_by_id("email").send_keys(email)
#            driver.find_element_by_id("telephone").send_keys(telephone)
#            driver.find_element_by_name("strPrivilegeName()").click()
#            driver.find_element_by_id("RegisterBut").click()
#            alert = self.driver.switch_to_alert()
#            alert.accept()
#            time.sleep(3)
#------------------------------注册用户成功------------------------------------------

#------------------------------授权用户------------------------------------------
        def accredit(ip):
            handle = driver.window_handles
            action_chains = ActionChains(driver)
            action_chains.move_to_element(driver.find_element_by_link_text("序列号管理")).perform()
            action_chains.click(driver.find_element_by_link_text("授权客户端")).perform()
            time.sleep(3)
            driver.find_element_by_id("nav")
            i = 2
            choose = ''
            #找匹配的ip
            ip0 = driver.find_elements_by_xpath("//div/table/tbody/tr[2]/td[3]")[0].text
            tmp = "//div/table/tbody/tr["+str(i)+"]/td[3]"
            while ip != ip0:
                i +=1;
                tmp = "//div/table/tbody/tr["+str(i)+"]/td[3]"
                ip0 = driver.find_elements_by_xpath(tmp)[0].text
            choose = "//div/table/tbody/tr["+str(i)+"]/td/input"
            #找匹配的ip成功

            #点击需授权/取消授权的记录
            driver.find_element_by_xpath(choose).click()
            time.sleep(2)

            #授权
            driver.find_element_by_id("addAuth").click()
            time.sleep(2)
            alert = self.driver.switch_to_alert()
            alert.accept()
            time.sleep(5)
            driver.switch_to_frame(1)
            driver.find_element_by_id("allCheckbox").click()
            time.sleep(5)
            driver.find_element_by_id("okBtn").click()
            time.sleep(2)
            alert = self.driver.switch_to_alert()
            alert.accept()
            #授权成功

            #取消授权
#            driver.find_element_by_id("cancelAuth").click()
#            driver.find_element_by_xpath("//div[2]/div[3]/button").click()
#            alert = self.driver.switch_to_alert()
#            alert.accept()
            #取消授权成功
#------------------------------授权用户------------------------------------------
        accredit("192.168.88.77")       
        time.sleep(5)
        driver.switch_to_window(handle)
        action_chains = ActionChains(driver)
        action_chains.move_to_element(driver.find_element_by_link_text("存储服务器")).perform()
        time.sleep(5)
        driver.switch_to_frame(0)
        time.sleep(5)
        driver.find_element_by_link_text("退出").click()
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()
