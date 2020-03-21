#!/usr/bin/env pythonw
# -*- coding: UTF-8 -*-
#


""" reception_page.py """

# --------------------------- GnrWebPage subclass ---------------------------
class GnrCustomWebPage(object):
    py_requires = """public:Public,th/th:TableHandler"""
    maintable = "bau.staff"
    css_requires = "bau"

    pageOptions = {"openMenu": False, "liveUpdate": True}

    def main(self, root, **kwargs):
        root = root.rootTabContainer(datapath="main", title=f"Gestione spesa {self.user}")
        self.richieste(root.contentPane(title='Richieste'))
        self.ordini(root.contentPane(title='Ordini'))

    def richieste(self,pane):
        pane.dialogTableHandler(table='shop.richiesta',
                                    viewResource='View',formResource='Form',
                                    view_store__onStart=True,datapath='.richieste')

    def ordini(self,pane):
        pane.dialogTableHandler(table='shop.ordine',view_store__onStart=True,datapath='.ordini',
                                viewResource='ViewFromVolontario',formResource='FormFromVolontario')