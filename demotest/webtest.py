# -*- coding:utf-8 -*-

from qt4i.device import Device
from demolib.demotestbase import DemoTestcase
from demolib.demoapp import DemoApp
from demolib.native.webwin import WebWin
from demolib.web.demopage import DemoPage

class WebTest(DemoTestcase):
    'Web App(demoapp 应用)测试'
    
    owner = 'hellertang'   #--------------------------------------------# 脚本的设计者
    priority = DemoTestcase.EnumPriority.Normal #-----------------------# 脚本的优先级
    status = DemoTestcase.EnumStatus.Design #-------------------------# 脚本的状态
    timeout = 5 #-------------------------------------------------# 脚本执行超时值 （分钟）
    
    def run_test(self):
        
        self.start_step('1、申请资源启动Demo app')
        device = Device()  #----------------------------------------# 申请测试设备
        demoapp = DemoApp(device) #------------------------------------# 启动被测试APP
        
        self.start_step('2、登录') 
        demoapp.login(user = "Qta", pwd = "123456") #------------------------------------# 登录demo app
        
        self.start_step('3、提交信息') 
        webwin =  WebWin(demoapp)
        page = DemoPage(webwin.webview) #------------------------------------# 初始化webpage
        page.set_name("qta")      
        page.set_age(str(20))
        page.set_company("tencent")
        page.set_female()
        page.submit()
        
        
if __name__ == '__main__':
    WebTest().debug_run()