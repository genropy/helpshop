#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nominativo_id')
        r.fieldcell('negozio_id')
        r.fieldcell('data_ordine')
        r.fieldcell('numero')
        r.fieldcell('note')
        r.fieldcell('mezzo_pagamento')
        r.fieldcell('ritiro_consegna')
        r.fieldcell('importo')
        r.fieldcell('fascia_oraria')

    def th_order(self):
        return 'nominativo_id'

    def th_query(self):
        return dict(column='numero', op='contains', val='')

    def th_options(self):
        return dict(partitioned=True)



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record')
        fb = top.formbuilder(cols=2, border_spacing='4px')
        fb.field('nominativo_id')
        fb.field('negozio_id')
        fb.field('data_ordine')
        fb.field('numero')
        fb.field('note')
        fb.field('mezzo_pagamento')
        fb.field('ritiro_consegna')
        fb.field('importo')
        fb.field('fascia_oraria')
        center = bc.contentPane(region='center')
        center.inlineTableHandler(relation='@righe')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
