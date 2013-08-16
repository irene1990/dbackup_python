#-*-coding=utf-8
from selenium import webdriver
import time
class Login:
    def __init__(self,Ip,UserN,Passwd,driver):
        self.ip = Ip
        self.username = UserN
        self.password = Passwd
        self.driver = driver
    def test_login(self):
        base_url = "http://"+self.ip+"/dbackup"
        self.driver.get(base_url)
        time.sleep(3)
        handle = self.driver.window_handles
        self.driver.switch_to_frame(0)
        self.driver.find_element_by_id("serialRadio").click()
        self.driver.find_element_by_id("trialRadio").click()
        self.driver.find_element_by_xpath("//div[3]/label").click()
        self.driver.find_element_by_id("continue").click()
        self.driver.switch_to_window(handle)
        self.driver.find_element_by_id("UserNameID").send_keys(self.username)
        self.driver.find_element_by_id("PWID").send_keys(self.password)
        self.driver.find_element_by_id("LoginButton").click()
        time.sleep(3)
        alert = self.driver.switch_to_alert()
#        print alert
#        if alert !="":
#            alert.accept()
        time.sleep(3)

