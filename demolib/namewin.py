# -*- coding:utf-8 -*-
'''
Created on 2018-10-23

'''
from qt4i.icontrols import Window
from qt4i.icontrols import Element
from qt4i.qpath import QPath


class NameWin(Window):
    '''DemoApp 注销登录页面
    '''

    def __init__(self, app):
        Window.__init__(self, app)
        self._device = self._app.device

        locators = {
              '更多信息': {'type': Element, 'root': self,
                      'locator': QPath("/classname = 'Button' & label = '更多信息' & visible = true & maxdepth = 11")},
              '输入框': {'type': Element, 'root': self,
                     'locator': QPath("/classname = 'TextField' & visible = true & maxdepth = 11")},
              '名称': {'type': Element, 'root': self,
                      'locator': 'qt4i'},
        }

        self.updateLocator(locators)

    def modify_name(self, name):
        '''
        '''
        self.Controls['更多信息'].click()
        name_text_field = self.Controls['输入框']
        name_text_field.click()
        name_text_field.value = name
        name_text_field.send_keys('\n')
        return self.Controls['名称'].exist()