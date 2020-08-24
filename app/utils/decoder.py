from datetime import datetime
from decimal import Decimal
from json import JSONEncoder

import pytz


class JsonDecoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        elif isinstance(obj, datetime):
            return obj.astimezone(tz=pytz.utc).strftime("%m/%d/%Y %H:%M:%S")
        elif isinstance(obj, bytes):
            return obj.decode()
        return JSONEncoder.default(self, obj)
