from app.models.users import User
from app.serializers import Serializer
from app.utils.descriptor import Int, String, DateTime, Bool


class UserSerializer(Serializer):
    id = Int(name="id")
    name = String(name="name")
    created_at = DateTime(name="created_at")
    updated_at = DateTime(name="updated_at")
    gender = Bool(name="gender")
    age = Int(name="age")

    def __init__(self, user: User):
        self.id = user.id
        self.name = user.name
        self.gender = user.gender
        self.age = user.age

