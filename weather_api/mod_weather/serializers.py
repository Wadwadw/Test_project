from datetime import date
from typing import Any

from sqlalchemy import inspect


class Serializer:
    def serialize(self) -> dict[Any, str]:
        dct = {}
        for key, value in inspect(self).attrs.items():
            if isinstance(value.value, date):
                dct[key] = date.strftime(value.value, '%Y-%m-%d')
            else:
                dct[key] = value.value
        return dct

    @staticmethod
    def serialize_list(lst):
        return [item.serialize() for item in lst]
