# encoding: utf-8

class Table(object):


    def trigger_onInserted(self, record):
        if record['in_out'] == 'I':
            self.insertRichiesta(record)

    def insertRichiesta(self,record=None):
        mittente,indirizzo_email =self.parsedAddress(record['from_address'])
        record_richiesta = dict(email=indirizzo_email,
                        nominativo=mittente, 
                        message_id=record['id'],
                        oggetto=record['subject'],
                        testo=record['body'])