# QT4i Demo项目

这是[QT4i](https://github.com/Tencent/qt4i)的Demo使用项目。

## 安装依赖库

    cd /path/to/project
    pip install -r requirements.txt

## 配置xctestagent

按照qt4i文档[快速入门](https://qt4i.readthedocs.io/zh_CN/latest/intro.html)指引，成功配置xctestagent。

## 执行Demo用例

    cd /path/to/project
    python manage.py runscript demotest/hello.py
