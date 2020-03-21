#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('__ins_ts',name='Data e ora')
        r.fieldcell('oggetto')
        r.fieldcell('nominativo')
        r.fieldcell('testo')
        r.fieldcell('message_id')
        r.fieldcell('ordine_id')

    def th_order(self):
        return 'oggetto'

    def th_query(self):
        return dict(column='oggetto', op='contains', val='')


    def th_top_custom(self,top):
        top.bar.replaceSlots('vtitle','2,sections@statorichiesta,*')

    def th_sections_statorichiesta(self):
        return [dict(code='da_consegnare',caption='Da esaminare',condition='$ordine_id IS NULL'),
                dict(code='esaminata',caption='Esaminata',condition='$ordine_id IS NOT NULL')]


class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer(datapath='.record')

        bc.contentPane(region='right',width='250px'
                                ).linkerBox('persona_id',
                                formResource='FormLinker',validate_notnull=True,
                                template='standard')
        fb = bc.contentPane(region='center').div(margin='5px',
                            margin_right='20px').formbuilder(cols=1, border_spacing='4px',
                                                                colswidth='auto',width='100%',
                                                                fld_width='100%',
                                                                max_width='500px')

        fb.field('oggetto')
        fb.field('nominativo')
        fb.field('email')
        fb.field('telefono')
        fb.field('testo',tag='simpleTextArea',height='80px')


    def th_options(self):
        return dict(dialog_height='240px', dialog_width='750px',modal=True)
