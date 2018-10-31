# -*- coding:utf-8 -*-
'''
Created on 2018-10-23

'''
from qt4i.device import Device
from demolib.demotestbase import DemoTestcase
from demolib.demoapp import DemoApp


class HelloTest(DemoTestcase):
    'Demo测试'

    owner = 'demo'  # --------------------------------------------# 脚本的设计者
    priority = DemoTestcase.EnumPriority.Normal  # -----------------------# 脚本的优先级
    status = DemoTestcase.EnumStatus.Design  # -------------------------# 脚本的状态
    timeout = 5  # -------------------------------------------------# 脚本执行超时值 （分钟）

    def run_test(self):
        self.start_step('1、申请资源启动DemoApp')
        device = Device()  # ----------------------------------------# 申请测试设备
        demoapp = DemoApp(device)  # ------------------------------------# 启动被测试APP

        self.start_step('2、查询设备信息')
        isEnter = demoapp.enter()  # -----------------------------# 进入设备信息页面
        self.assertEqual("检验是否查看成功", isEnter, True)  # -----------------------------# 检查是否进入成功

        self.start_step('3、修改设备名称')
        name = 'qt4i'
        isModify = demoapp.rename(name)  # -----------------------------# 修改设备名称
        self.assertEqual("检验是否修改成功", isModify, True)  # -----------------------------# 检查是否修改成功


if __name__ == '__main__':
    HelloTest().debug_run()

