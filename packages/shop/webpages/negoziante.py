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
        negozio = self.rootenv['nome_negozio']
        root = root.rootContentPane(datapath="main", title=f"Gestione ordini di {negozio}")
        self.ordini(root)

    def ordini(self,pane):
        pane.dialogTableHandler(table='shop.ordine',view_store__onStart=True,datapath='.ordini')