
from gnr.web.gnrwebpage import BaseComponent
import datetime

class LoginComponent(BaseComponent):
    def onAuthenticating_shop(self, avatar, rootenv=None):
        negozio_id,nome_negozio = self.db.table('adm.user'
                                    ).readColumns(pkey=avatar.user_id,
                                        columns="$negozio_id,@negozio_id.nome")

        if negozio_id:
            rootenv['nome_negozio'] = nome_negozio
            rootenv['negozio_id'] = negozio_id
            rootenv['current_negozio_id'] = negozio_id
