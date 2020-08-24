from _decimal import Decimal
from datetime import datetime
from dateutil.parser import parse
import decimal

import pytz


class Bool:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if type(value) != bool:
            raise ValueError(f"{self.name} type error: {value}")
        instance.__dict__[self.name] = value


class Int:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if value_type == Decimal or value_type == str or value_type == float:
                value = int(value)
            elif value_type != int:
                raise ValueError(f"{self.name} type error: {value_type}")
            instance.__dict__[self.name] = value


class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if value_type != str:
                raise ValueError(f"{self.name} type error: {value_type}")
            instance.__dict__[self.name] = value


class IsoFormatDatetime:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if value_type == datetime:
                instance.__dict__[self.name] = value.replace(
                    tzinfo=pytz.utc
                ).isoformat()
            elif value_type == str:
                instance.__dict__[self.name] = parse(value)
            else:
                raise ValueError(f"{self.name} type error: {value_type}")


class UnixTimestamp:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if value_type == datetime:
                instance.__dict__[self.name] = int(value.timestamp())
            elif value_type == str:
                instance.__dict__[self.name] = int(parse(value).timestamp())
            elif value_type == Decimal:
                time_obj = datetime.fromtimestamp(value)
                instance.__dict__[self.name] = int(time_obj.timestamp())
            else:
                instance.__dict__[self.name] = int(datetime.now().timestamp())


class DateTime:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if value_type == datetime:
                instance.__dict__[self.name] = value.replace(
                    tzinfo=pytz.utc
                ).strftime("%Y-%m-%d %H:%M:%S")
            elif value_type == str:
                instance.__dict__[self.name] = parse(value)
            else:
                raise ValueError(f"{self.name} type error: {value_type}")


class List:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if value_type != list:
                raise ValueError(f"{self.name} type error: {value_type}")
            instance.__dict__[self.name] = value


class Float:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if value_type == int or value_type == str:
                value = float(value)
            elif value_type != float:
                raise ValueError(f"{self.name} type error: {value_type}")
            instance.__dict__[self.name] = value


class Decimal:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if value_type == int or value_type == str or value_type == float:
                value = decimal.Decimal(value)
            elif value_type != decimal.Decimal:
                raise ValueError(f"{self.name} type error: {value_type}")
            instance.__dict__[self.name] = value


class BuyActionType:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if value_type == str:
                value = BuyAction[value]
            elif value_type != BuyAction:
                raise ValueError(f"{self.name} type error: {value_type}")

            instance.__dict__[self.name] = value


class SubscriptionStatusType:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if value_type == str:
                value = SubscriptionStatus[value]
            elif value_type != SubscriptionStatus:
                raise ValueError(f"{self.name} type error: {value_type}")

            instance.__dict__[self.name] = value


class EVendorType:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if value_type == str:
                value = EVendorId[value]
            elif value_type != EVendorId:
                raise ValueError(f"{self.name} type error: {value_type}")

            instance.__dict__[self.name] = value


class UpdatedReasonCodeType:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if value_type == str:
                value = UpdatedReasonCode[value]
            elif value_type != UpdatedReasonCode:
                raise ValueError(f"{self.name} type error: {value_type}")

            instance.__dict__[self.name] = value


class OrderActionType:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if value_type == str:
                value = OrderAction[value]
            elif value_type != OrderAction:
                raise ValueError(f"{self.name} type error: {value_type}")

            instance.__dict__[self.name] = value


class EVendorIdType:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value:
            value_type = type(value)
            if value_type == str:
                value = EVendorId[value]
            elif value_type != EVendorId:
                raise ValueError(f"{self.name} type error: {value_type}")

            instance.__dict__[self.name] = value
