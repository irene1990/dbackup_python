#-*-coding=utf-8
from selenium.webdriver import ActionChains
import time,re,unittest
class User(unittest.TestCase):
    def __init__(self,driver):
        print "You are in User Module now"
        self.driver = driver 
        self.action_chains = ActionChains(self.driver)
        time.sleep(3)
        self.action_chains.move_to_element(self.driver.find_element_by_link_text("用户管理")).perform()
#--------------------------------增加用户---------------------------
    def AddUser(self,name,password,email,tel,privilege):
         time.sleep(5)
         self.action_chains.click(self.driver.find_element_by_link_text("注册用户")).perform()
         time.sleep(3)
         self.driver.find_element_by_id("username").send_keys(name)
         self.driver.find_element_by_id("strPassword").send_keys(password)
         self.driver.find_element_by_id("confirmpassword").send_keys(password)
         self.driver.find_element_by_id("email").send_keys(email)
         self.driver.find_element_by_id("telephone").send_keys(tel)
         #privilege——1:系统权限；2:上级监控；3:备份恢复；4:查看报表
         i = 1
         while i<5:
             tmp = re.search(str(i),privilege)
             time.sleep(1)
             if(tmp == None):
                 if i != 1:
                     self.driver.find_element_by_xpath("(//input[@name='strPrivilegeName[]'])["+str(i)+"]").click()
                 #time.sleep(2)
             elif i == 1:
                 self.driver.find_element_by_name("strPrivilegeName[]").click()
             i += 1
         self.driver.find_element_by_id("RegisterBut").click()
         alert = self.driver.switch_to_alert()
         time.sleep(2)
         alert.accept()
         print self.driver.current_url
         self.driver.refresh()
         time.sleep(2)
#--------------------------------增加用户成功--------------------

#--------------------------------删除用户------------------------
    def DeleteUser(self,user,alert):
        self.action_chains.move_to_element(self.driver.find_element_by_link_text("用户管理")).perform()
        time.sleep(1)
        self.action_chains.click(self.driver.find_element_by_link_text("所有用户")).perform()
        time.sleep(3)
        #其实需要判断当前用户是否属于admin用户的
        self.ChooseUser(user)
        self.driver.find_element_by_id("nDeleteAccountID").click()
        time.sleep(2)    
        #alert = raw_input('Do you really want to delete?[y/n]')
        self.AlertWin(alert)  
#--------------------------------删除用户成功------------------------        

#--------------------------------锁定用户------------------------
    def LockUser(self,user,alert):
        self.action_chains.click(self.driver.find_element_by_link_text("所有用户")).perform()
        time.sleep(3)
        t = user.split(';')
        l = len(t)
        i = 0
        while i < l:
            self.ChooseUser(t[i])
            self.driver.find_element_by_id("nLockAccountID").click()
            time.sleep(2)
            self.AlertWin(alert)
            i +=1
#--------------------------------锁定用户成功--------------------

#--------------------------------解锁用户------------------------        
    def UnlockUser(self,user,alert):
        self.action_chains.move_to_element(self.driver.find_element_by_link_text("用户管理")).perform()
        time.sleep(1)
        self.action_chains.click(self.driver.find_element_by_link_text("所有用户")).perform()
        time.sleep(3)
        t = user.split(';')
        l = len(t)
        i = 0
        while i < l:
            self.ChooseUser(t[i])
            self.driver.find_element_by_id("nUnLockAccountID").click()
            time.sleep(2)
            self.AlertWin(alert)
            i +=1
#--------------------------------解锁用户成功--------------------

#--------------------------------修改客户----------------------
    def ModifidUser(self,user,email,tel,privilege):
        self.action_chains.move_to_element(self.driver.find_element_by_link_text("用户管理")).perform()
        time.sleep(1)
        self.action_chains.click(self.driver.find_element_by_link_text("所有用户")).perform()
        time.sleep(3)
        self.ChooseUser(user)
        self.driver.find_element_by_id("nModifyID").click()
        time.sleep(3)
        self.driver.find_element_by_id("nEmailID").send_keys(email)
        self.driver.find_element_by_id("telephone").send_keys(tel)
        li = ["nPriSysBoxID","nPriMonitorBoxID","nPriBackupBoxID","nPriReportBoxID"]
        i = 0
        while i < len(li):
            tmp = re.search(str(i+1),privilege)
            if tmp !=None:
                self.driver.find_element_by_id(li[i]).click()
                print li[i]
            i +=1
        time.sleep(2)
        self.driver.find_element_by_id("nSubmitModifyButID").click()
        alert = self.driver.switch_to_alert()
        time.sleep(2)
        alert.accept()
        time.sleep(2)

#--------------------------------客户端访问----------------------
    def VisitedCient(self,user,client):
        #self.action_chains.click(self.driver.find_element_by_link_text("所有用户")).perform()
        time.sleep(2)
        self.ChooseUser(user)
        self.driver.find_element_by_id("accessAcount").click()
        handle = self.driver.window_handles
        self.driver.switch_to_frame(1)
        time.sleep(3)
        tclient = client.split(';')
        l = len(tclient)
        k = 0
        while k < l:
        #这里的一种可能性是有些client在迪备中并不存在。这个要加判断，算了，这个不加了。既然是测试人员测试，那么这里输入的值必须为有效值才行！
            #该客户端是否已处于被选中状态
            m = self.driver.find_element_by_xpath("(//label[@title='"+tclient[k]+"']/input)").get_attribute("checked")
            if m == None:
                self.driver.find_element_by_xpath("(//label[@title='"+tclient[k]+"']/input)").click()
            k +=1
        self.driver.find_element_by_id("okBtn").click()
        #self.driver.find_element_by_id("cancelBtn").click()
        time.sleep(2)
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(2)
#--------------------------------客户端访问成功-----------------

#--------------------------------选择用户-----------------------
    def ChooseUser(self,user):
        print 'ChooseUser'
        ii = 2
        tmp = ' '
        while (cmp(tmp,user)!=0):
            tmp = self.driver.find_element_by_xpath("//div/table/tbody/tr["+str(ii)+"]/td[2]").text
            ii +=1
        self.driver.find_element_by_id("RadioID"+str(ii-3)+"").click()
        time.sleep(2)
#--------------------------------选择用户成功-------------------

#------------------------------- 确定取消操作--------------------
    def AlertWin(self,a):
        alert = self.driver.switch_to_alert()
        #alert_text = alert.text
        time.sleep(3)
        if a == 'y':
            alert.accept()
            time.sleep(2)
            alert = self.driver.switch_to_alert()
            time.sleep(2)
            alert.accept()
            time.sleep(2)
        else:
            alert.dismiss()
        time.sleep(3)
