# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('persona',pkey='id',name_long='Persona',name_plural='Persone',caption_field='nominativo')
        self.sysFields(tbl)
        tbl.column('nominativo',name_long='Nominativo')
        tbl.column('indirizzo',name_long='Indirizzo')
        tbl.column('geocoder',name_long='Geocoder')
        tbl.column('telefono',name_long='Telefono')
        tbl.column('email',name_long='Email')
        tbl.column('w3w',name_long='W3W')
