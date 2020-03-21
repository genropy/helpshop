#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('data_ordine')
        r.fieldcell('negozio_id')
        r.fieldcell('nominativo_id')
        r.fieldcell('numero')
        r.fieldcell('note')
        r.fieldcell('mezzo_pagamento')
        r.fieldcell('ritiro_consegna')
        r.fieldcell('importo')
        r.fieldcell('fascia_oraria')

    def th_order(self):
        return 'data_ordine'

    def th_query(self):
        return dict(column='numero', op='contains', val='')


    def th_options(self):
        return dict(partitioned=True)
    
    def th_top_custom(self,top):
        top.slotToolbar('sections@statoordine,*,sections@fascia_oraria,10,sections@ritiro_consegna',childname='upper',_position='<bar')

    def th_sections_statoordine(self):
        return [dict(code='da_consegnare',caption='Da consegnare',condition='$consegna_ts IS NULL'),
                dict(code='consegnato',caption='Consegnato',condition='$consegna_ts IS NOT NULL')]


class ViewFromNegozio(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('data_ordine')
        r.fieldcell('nominativo_id')
        r.fieldcell('numero')
        r.fieldcell('note')
        r.fieldcell('mezzo_pagamento')
        r.fieldcell('ritiro_consegna')
        r.fieldcell('importo')
        r.fieldcell('fascia_oraria')

    def th_order(self):
        return 'data_ordine'

    def th_sections_statoordine(self):
        return [dict(code='da_consegnare',caption='Da consegnare',condition='$consegna_ts IS NULL'),
                dict(code='consegnato',caption='Consegnato',condition='$consegna_ts IS NOT NULL')]

    def th_top_custom(self,top):
        top.bar.replaceSlots('vtitle','2,sections@statoordine,10,sections@fascia_oraria,10,sections@ritiro_consegna')


class ViewFromVolontario(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('data_ordine')
        r.fieldcell('negozio_id')
        r.fieldcell('nominativo_id')
        r.fieldcell('numero')
        r.fieldcell('note')
        r.fieldcell('mezzo_pagamento')
        r.fieldcell('ritiro_consegna')
        r.fieldcell('importo')
        r.fieldcell('fascia_oraria')

    def th_order(self):
        return 'data_ordine'

    def th_sections_statoordine(self):
        return [dict(code='da_consegnare',caption='Da consegnare',condition='$consegna_ts IS NULL'),
                dict(code='consegnato',caption='Consegnato',condition='$consegna_ts IS NOT NULL')]

    def th_top_custom(self,top):
        top.bar.replaceSlots('vtitle','2,sections@statoordine,10,sections@fascia_oraria,10,sections@ritiro_consegna')


class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.borderContainer(region='top',datapath='.record',height='150px')
        top.contentPane(region='left',width='250px'
                                ).linkerBox('nominativo_id',
                                formResource='FormLinker',validate_notnull=True,
                                template='standard')
        fb = top.contentPane(region='center').div(margin='5px',
                            margin_right='20px').formbuilder(cols=2, border_spacing='4px',
                                                                colswidth='auto',width='100%',
                                                                fld_width='100%',
                                                                max_width='800px')
        fb.field('data_ordine',width='7em')
        fb.field('numero',width='7em')
        fb.field('mezzo_pagamento')
        fb.field('ritiro_consegna')
        fb.field('fascia_oraria')
        fb.field('importo',width='7em')
        fb.field('data_consegna',width='7em')
        fb.field('ora_consegna',width='7em')
        fb.field('note',colspan=2,tag='simpleTextArea')
        center = bc.contentPane(region='center')
        center.inlineTableHandler(relation='@righe')

    @public_method
    def th_onLoading(self, record, newrecord, loadingParameters, recInfo):
        if newrecord:
            record['negozio_id'] = record['negozio_id'] or self.db.currentEnv.get('current_negozio_id')
            record['data_ordine'] = self.db.workdate

    def th_options(self):
        return dict(dialog_parentRatio=0.9)

class FormFromNegoziante(Form):
    def th_options(self):
        return dict(dialog_parentRatio=0.9)


class FormFromVolontario(Form):

    def th_options(self):
        return dict(dialog_parentRatio=0.9,defaultPrompt=dict(
                title="Nuova valutazione",
                fields=[
                    dict(
                        value="^.negozio_id",
                        tag="dbselect",
                        lbl="Negozio",
                        validate_notnull=True,
                        width="15em",
                        dbtable="shop.negozio",
                        hasDownArrow=True,
                    )
                ],
                doSave=True,
            ))
