# -*- coding: utf-8 -*-

from qt4i.icontrols import Window
from qt4i.qpath import QPath
from qt4i.web import IOSWebView


class WebWin(Window):
    '''窗口基类(包含WebView)
    '''
    def __init__(self, app):
        self._app = app
        self._device = self._app.device
        Window.__init__(self, self._app)
        self.scroll_win = Window(self._app, "ScrollView")
        locators = {
            'webview' : {'type':IOSWebView, 'root':self.scroll_win, 'locator':QPath("/classname='Other'")},
        }
        self.updateLocator(locators)
    
    @property
    def webview(self):
        '''WebView对象
        '''        
        return self.Controls['webview']
