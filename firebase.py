import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
from database_meta import DataBaseMeta


class FireBase(metaclass=DataBaseMeta):

    def __init__(self, name: str):
        self.conection()
        self.__db = firestore.client()
        self.__name = name

    def read(self):
        pass

    def write(self, text: str, type_msg: str):
        fecha: str = datetime.now().strftime('%d-%m-%Y')
        hora: str = datetime.now().strftime('%H:%M:%S')
        name_doct: str = "[" + fecha + " " + hora + "]  >> " + type_msg
        doc_ref = self.__db.collection(self.__name).document(name_doct)
        data = {
            u'Tipo': type_msg,
            u'Fecha': fecha,
            u'Hora': hora,
            u'Mensaje': text
        }
        doc_ref.set(data)

    def conection(self):
        cred = credentials.Certificate('Clave.json')
        firebase_admin.initialize_app(cred)

    def close_conection(self):
        pass