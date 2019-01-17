# QT4i Demo项目

这是[QT4i](https://github.com/Tencent/qt4i)的Demo使用项目。

主要提供两种App的Demo示例，主要提供两类App的demo用例: 系统自带设置应用(native)和[DemoApp](https://github.com/qtacore/QT4iDemoApp)(webview)

## 安装依赖库

    cd /path/to/project
    pip install -r requirements.txt

## 配置xctestagent

按照qt4i文档[快速入门](https://qt4i.readthedocs.io/zh_CN/latest/intro.html)指引，成功配置xctestagent。

## 执行Demo用例

    
    cd /path/to/project
    #对应setting.py中APP_BUNDLE_ID = "com.apple.Preferences"   
    python manage.py runscript demotest/native.py
    #对应setting.py中APP_BUNDLE_ID = "com.tencent.demoapp"，需先安装demoapp  
    python manage.py runscript demotest/web.py
