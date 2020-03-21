# encoding: utf-8

class Table(object):


    def trigger_onInserted(self, record):
        if record['in_out'] == 'I':
            subject = record['subject']
            if subject and subject.upper().startswith('NEGOZIO'):
                self.insertRichiesta(record,subject=subject[10:])
            elif subject and subject.upper().startswith('AGGIORNAMENTO'):
                self.insertRichiesta(record,subject=subject[13:], aggiornamento=True)
            email_bag = record['email_bag']
            if subject == 'Re: Richiesta ulteriori informazioni sul suo profilo' or email_bag['In-Reply-To']:
                self.aggiornaRichiesta(record)
