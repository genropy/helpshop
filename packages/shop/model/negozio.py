# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('negozio',pkey='id',name_long='Negozio',
                        name_plural='Negozio',caption_field='nome')
        self.sysFields(tbl)
        tbl.column('nome',name_long='Nome')
        tbl.column('indirizzo',name_long='Indirizzo')
        tbl.column('telefono',name_long='Telefono')
        tbl.column('iban', name_long='IBAN')
        tbl.column('nominativo', name_long='Nominativo')
        tbl.column('tipologia', size=':2', name_long='Tipologia',
                    values='S:Supermercato,V:Verdure,P:Panettiere,A:Altro') 
        tbl.column('descrizione', name_long='Descrizione')
        tbl.column('geocoder', name_long='Geocoder')

    

    def partitionioning_pkeys(self):
        return [r['id'] for r in self.query().fetch()]