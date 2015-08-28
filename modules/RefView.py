from PyQt5 import QtWebKitWidgets


class RefView(QtWebKitWidgets.QWebView):

    def __init__(self, parent):
        super(RefView, self).__init__(parent)
