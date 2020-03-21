# encoding: utf-8
from gnr.core.gnrdecorator import metadata
class Table(object):

    @metadata(mandatory=True)
    def sysRecord_NEGOZIANTE(self):
        return self.newrecord(code='NEGOZIANTE',
                            description='Addetto negozio',
                            rootpage='/shop/negoziante')
    
    @metadata(mandatory=True)
    def sysRecord_VOLONTARIO(self):
        return self.newrecord(code='VOLONTARIO',
                            description='Volontario',
                            rootpage='/shop/volontario')