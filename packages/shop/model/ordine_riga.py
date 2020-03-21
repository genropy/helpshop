# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('ordine_riga',pkey='ordine_id',name_long='Riga ordine',name_plural='Righe ordine',caption_field='ordine_id')
        tbl.column('ordine_id',size='22',name_long='Ordine').relation('ordine.id',relation_name='righe', mode='foreignkey', onDelete='cascade', meta_thmode='dialog')
        tbl.column('prodotto',name_long='Prodotto')
        tbl.column('quantita',name_long='Quantità')
        tbl.column('note',name_long='Note')
