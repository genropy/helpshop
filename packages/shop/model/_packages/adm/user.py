# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('user')
        tbl.column('negozio_id',size='22', group='_', name_long='Negozio',plugToForm=True
                    ).relation('shop.negozio.id', relation_name='external_users',
                                mode='foreignkey', onDelete='raise')        
                                