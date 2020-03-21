# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('prodotto_tipo',pkey='descrizione',name_long='Prodotto tipo',name_plural='Prodotto tipo',caption_field='descrizione',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('descrizione',name_long='Descrizione')