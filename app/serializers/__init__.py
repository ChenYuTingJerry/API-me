class Serializer:
    def __init__(self, obj=None, **kwargs):
        if not obj:
            obj = kwargs
        for k, v in obj.items():
            self.__setattr__(k, v)

    def to_dict(self):
        result = {}
        for k, v in self.__dict__.items():
            if v is not None and not k.startswith("_"):
                if isinstance(v, Serializer):
                    result[k] = v.to_dict()
                else:
                    result[k] = v
        return result
