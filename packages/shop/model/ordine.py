# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('ordine',pkey='id',name_long='Ordine',name_plural='Ordine',
                        caption_field='numero',partition_negozio_id='negozio_id')
        self.sysFields(tbl,user_upd=True)
        tbl.column('nominativo_id',size='22',name_long='Nominativo').relation('persona.id',relation_name='ordini', mode='foreignkey', onDelete='raise', meta_thmode='dialog')
        tbl.column('negozio_id',size='22',name_long='Negozio').relation('negozio.id',relation_name='ordini', mode='foreignkey', onDelete='raise', meta_thmode='dialog')
        tbl.column('data_ordine',dtype='D',name_long='Data ordine')
        tbl.column('numero',size=':10',name_long='Numero')
        tbl.column('note',name_long='Note')
        tbl.column('mezzo_pagamento',size='2',name_long='Mezzo di pagamento',values='C:Contanti,P:POS,BO:Bonifico')
        tbl.column('ritiro_consegna',size='1',name_long='Ritiro consegna',values='R:Ritiro,C:Consegna')
        tbl.column('importo',dtype='N',name_long='Importo totale')
        tbl.column('fascia_oraria',size='1',name_long='Fascia oraria',values='M:Mattino,P:Pomeriggio')
        tbl.column('priorità', dtype='L', name_long='Priorità')
        tbl.column('ragione', name_long='Ragione')
        tbl.column('data_consegna',dtype='D',name_long='Data consegna')
        tbl.column('consegna_ts',dtype='DH',name_long='Consegnato il')

