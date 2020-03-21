#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nominativo')
        r.fieldcell('indirizzo')
        r.fieldcell('geocoder')
        r.fieldcell('telefono')
        r.fieldcell('email')
        r.fieldcell('w3w')

    def th_order(self):
        return 'nominativo'

    def th_query(self):
        return dict(column='nominativo', op='contains', val='')


class FormLinker(BaseComponent):
    def th_form(self, form):
        pane = form.record
        fb = pane.div(margin='10px',
                    margin_right='20px').formbuilder(cols=1, 
                                border_spacing='4px',
                                colswidth='auto',
                                width='100%',fld_width='100%')
        fb.field('nominativo')
        fb.field('telefono')
        fb.field('email')
        fb.field('indirizzo', tag='geoCoderField',
                 lbl='Indirizzo',
                 #selected_street_address='.indirizzo_',
                 selected_locality='.localita',
                 selected_position='.geocoder',
                 ghost=u'Strada, Numero, Località')         
        fb.field('w3w')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' ,modal=True)

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('nominativo' )
        fb.field('indirizzo' )
        fb.field('geocoder' )
        fb.field('telefono' )
        fb.field('email' )
        fb.field('w3w' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
