# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('richiesta', pkey='id', name_long='Richiesta', name_plural='Richieste',caption_field='oggetto')
        self.sysFields(tbl)
        tbl.column('oggetto', name_long='Oggetto')
        tbl.column('nominativo', name_long='Nominativo')
        tbl.column('testo', name_long='Testo')
        tbl.column('email', name_long='Email')
        tbl.column('telefono', name_long='Telefono')
        tbl.column('message_id',size='22', group='_', name_long='Messaggio email'
                    ).relation('email.message.id',
                                mode='foreignkey', onDelete='raise')
        tbl.column('ordine_id',size='22', group='_', name_long='Ordine'
                    ).relation('ordine.id', mode='foreignkey', onDelete='raise')
        tbl.column('persona_id',size='22', group='_', name_long='Persona'
                    ).relation('persona.id', relation_name='richieste', mode='foreignkey', onDelete='raise')