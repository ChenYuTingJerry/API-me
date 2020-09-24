import json
from datetime import datetime
from decimal import Decimal

from dateutil.parser import parse

import pytz


class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError(f"{self.name} type error: {type(value)}")
        instance.__dict__[self.name] = value


class IsoFormatDatetime:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if type(value) == datetime:
            instance.__dict__[self.name] = value.replace(
                tzinfo=pytz.utc
            ).isoformat()
        elif type(value) == str:
            instance.__dict__[self.name] = (
                parse(value).replace(tzinfo=pytz.utc).isoformat()
            )
        else:
            raise ValueError(f"{self.name} type error: {type(value)}")


class JSON:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if type(value) == dict:
            instance.__dict__[self.name] = json.dumps(
                value, ensure_ascii=False
            )
        elif type(value) == list:
            instance.__dict__[self.name] = json.dumps(
                value, ensure_ascii=False
            )
        elif type(value) == str:
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f"{self.name} type error: {type(value)}")


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if type(value) == int:
            instance.__dict__[self.name] = value
        elif type(value) == Decimal:
            instance.__dict__[self.name] = int(value)
        else:
            raise ValueError(f"{self.name} type error: {type(value)}")
