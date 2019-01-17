# -*- coding:utf-8 -*-

from qt4i.icontrols import App
from testbase.conf import settings
from demolib.native.infowin import InfoWin
from demolib.native.namewin import NameWin
from demolib.native.loginwin import LoginWin


class DemoApp(App):
    '''DemoApp 负责被测应用的启动和初始化
    '''

    def __init__(self, device, app_name=settings.APP_BUNDLE_ID, trace_template=None, trace_output=None):
        '''APP应用（启动APP）

        :param device         : Device的实例对象
        :type device          : Device
        :param app_name       : APP的BundleID（例如：com.tencent.sng.test.gn）
        :type app_name        : str
        :param trace_template : trace模板（专项测试使用，功能测试默认为None即可）
        :type trace_template  : str
        :param trace_output   : teace存储路径（专项测试使用，功能测试默认为None即可）
        :type trace_output    : str
        '''

        App.__init__(self, device, app_name, trace_template, trace_output)
        self.set_environment()
        self.start()

    def set_environment(self):
        '''初始化自动处理Alert弹框应对规则

        :param: none
        :returns: none
        '''
        # 此规则用于处理预期内容但难以预期弹出时机的Alert框（注意国际化多国语言的情况）。
        # 配置策略后，只要Alert框命中策略，即按策略处理。例如指定点击取消或确定按钮。
        self.rules_of_alert_auto_handle = [

            # 推送通知
            {
                'message_text': '推送通知|Notifications',  # 支持正则表达式
                'button_text': '^好$|^Allow$|^允许$'  # 支持正则表达式
            },

        ]

        # 此开关打开，用于处理不可预期内容且不可预期时机的Alert框
        # 如果Alert框命中上方的策略，则此项配置将被跳过。
        self.flag_alert_auto_handled = False

    def enter(self):
        '''进入设备信息函数
        '''
        infoWin = InfoWin(self)
        return infoWin.enter_info()

    def rename(self, name):
        '''修改设备名称函数
        '''
        nameWin = NameWin(self)
        return nameWin.modify_name(name)
    
    def login(self, user, pwd):
        '''登录
        '''
        loginWin = LoginWin(self)
        return loginWin.login(user, pwd)
        
