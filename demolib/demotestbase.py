# -*- coding:utf-8 -*-
'''
Created on 2018-10-23

'''
from qt4i.itestcase import iTestCase
from qt4i.device    import Device
from testbase.conf import settings


class DemoTestcase(iTestCase):
    '''Demo测试用例基类
    '''

    def pre_test(self):
        '''初始化测试用例
        '''
        super(iTestCase, self).pre_test()
        self.log_info("%s.pre_test "%self.__class__.__name__)

    def post_test(self):
        '''清理下测试用例
        '''
        super(iTestCase, self).post_test()
        self.clean_login()
        self.log_info("%s.post_test "%self.__class__.__name__)
        
    def clean_login(self):
        '''清理App的登录状态
        '''
        for device in Device.Devices:
            device.remove_file(settings.APP_BUNDLE_ID, "/Documents/contents/DemoAccountManager")