# -*- coding: utf-8 -*-

from qt4w import XPath
from qt4w.webcontrols import  WebPage, WebElement, InputElement,SelectElement

class DemoPage(WebPage):
    '''Demoapp web页面
    '''
    ui_map = {
                'title':{'type': WebElement,'locator': XPath('//div[@class="panel-heading"]')},
                'name':{'type': InputElement,'locator':XPath('//input[@id="name"]')},
                'female':{'type': WebElement,'locator':XPath('//input[@value="female"]')},
                'male':{'type': WebElement,'locator':XPath('//input[@value="male"]')},
                'age':{'type': SelectElement,'locator':XPath('//select[@id="age"]')},
                'company':{'type': InputElement,'locator':XPath('//input[@id="company"]')},
                'submit':{'type': WebElement,'locator':XPath('//button[@id="submit"]')},
            }
    
    #设置姓名
    def set_name(self,name):
        print self.control('name').exist()
        self.control('name').value=name
        
    #设置性别
    def set_female(self):
        self.control('female').click();
    
    def set_male(self):
        self.control('male').click();
         
    #设置姓名
    def set_age(self,age):
        self.control('age').selection=age
        
    #设置公司名
    def set_company(self,company):
        self.control('company').value=company
    
    #提交结果
    def submit(self):
        self.control("submit").click()
