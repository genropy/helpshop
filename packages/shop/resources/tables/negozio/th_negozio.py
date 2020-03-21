#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome')
        r.fieldcell('indirizzo')
        r.fieldcell('telefono')
        r.fieldcell('iban')
        r.fieldcell('nominativo')
        r.fieldcell('tipologia')
        r.fieldcell('descrizione')
        r.fieldcell('geocoder')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')



class Form(BaseComponent):
    py_requires='extuser_manager:ExternalUsers'
    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top').div(margin='10px',
                    margin_right='20px'
                    ).formbuilder(cols=2, border_spacing='4px',fld_width='100%',
                                    width='100%',colswidth='auto',max_width='800px',
                                    datapath='.record')
        fb.field('nome',colspan=2)
        fb.field('indirizzo', tag='geoCoderField',colspan=2,
                 lbl='Indirizzo',
                 #selected_street_address='.indirizzo_',
                 selected_locality='.localita',
                 selected_position='.geocoder',
                 ghost=u'Strada, Numero, Località')  
        fb.field('telefono')
        fb.field('tipologia')
        fb.field('nominativo',lbl='Nominativo')
        fb.field('iban')
        fb.field('descrizione',tag='simpleTextArea',height='200px',colspan=2)
        tc = bc.tabContainer(region='center',margin='2px')
        tc.externalUsers(title='Utenti',default_group_code='NEGOZIANTE')
        tc.contentPane(title='Ordini').dialogTableHandler(relation='@ordini',
                                                        viewResource='ViewFromNegozio')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
