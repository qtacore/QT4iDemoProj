#-*- coding:utf-8 -*-

from qt4i.icontrols import Window
from qt4i.icontrols import Element
from qt4i.qpath import QPath


class LoginWin(Window):
    '''DemoApp 登录页面
    '''

    def __init__(self, app):
        Window.__init__(self, app)
        self._device = self._app.device

        locators = {
              'logo': {'type': Element, 'root': self,
                      'locator': 'logo'},   
              '用户': {'type': Element, 'root': self,
                      'locator': 'email'},
              '密码': {'type': Element, 'root': self,
                     'locator': 'password'},
              '登录': {'type': Element, 'root': self, 
                     'locator': '登录'},
        }

        self.updateLocator(locators)

    def login(self, user, pwd):
        '''登录
        '''
        user_text_field = self.Controls['用户']
        user_text_field.click()
        user_text_field.value = user
        user_text_field.send_keys('\n')
        pwd_text_field = self.Controls['密码']
        pwd_text_field.click()
        pwd_text_field.send_keys('%s\n' %pwd)
        self.Controls['logo'].click()
        self.Controls['登录'].click()
        return not self.Controls['logo'].exist