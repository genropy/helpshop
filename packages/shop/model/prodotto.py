# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('prodotto',pkey='id',name_long='Prodotto',name_plural='Prodotti',caption_field='id')
        self.sysFields(tbl)
        tbl.column('descrizione',name_long='descrizione')
        tbl.column('tipo',name_long='tipo')