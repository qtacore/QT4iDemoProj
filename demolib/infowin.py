# -*- coding:utf-8 -*-
'''
Created on 2018-10-23

'''

from qt4i.icontrols import Window
from qt4i.icontrols import Element
from qt4i.qpath import QPath


class InfoWin(Window):
    '''DemoApp 输入登录页面
    '''

    def __init__(self, app):
        Window.__init__(self, app)
        self._device = self._app.device

        locators = {
            '通用': {'type': Element, 'root': self,
                      'locator': QPath("/classname = 'Cell' & label = '通用' & maxdepth = 7")},
            '关于本机': {'type': Element, 'root': self,
                         'locator': QPath("/classname = 'StaticText' & label = '关于本机' & visible = true & maxdepth = 12")},
            '名称': {'type': Element, 'root': self,
                     'locator': QPath("/classname = 'StaticText' & label = '名称' & visible = true & maxdepth = 11")},

#             "Table": {"type": Element, "root": self,
#                               "locator": QPath("/classname = 'Table' & visible = true & maxdepth = 10")},
#             "名称": {"type": Element, "root": "@Table",
#                       "locator": QPath("/classname='StaticText' & label ='名称' & maxdepth = 1")},
        }

        self.updateLocator(locators)

    def enter_info(self):
        '''账号密码输入登录函数
        '''
        self.Controls['通用'].click()
        self.Controls['关于本机'].click()
        return self.Controls['名称'].exist()
