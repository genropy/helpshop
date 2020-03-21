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
