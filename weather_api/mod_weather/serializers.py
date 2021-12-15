from datetime import date

from sqlalchemy import inspect



class Serializer(object):

    def serialize(self):
        dct = {}
        for key, value in inspect(self).attrs.items():
            if isinstance(value.value, date):
                dct[key] = date.strftime(value.value, '%Y-%m-%d')
            else:
                dct[key] = value.value
        return dct

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
