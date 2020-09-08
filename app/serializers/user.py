from app.model.picture import NormalPicture
from app.model.user import User
from app.serializers import Serializer
from app.serializers.image import NormalPictureSerializer
from app.utils.descriptor import Integer, String


class BlockUserSerializer(Serializer):
    id: Integer
    name: String
    age: Integer
    v_level: Integer
    picture: NormalPictureSerializer

    def __init__(self, user: User, normal_picture: NormalPicture):
        self.id = user.id
        self.name = user.name
        self.age = user.age
        self.v_level = 0
        self.picture = NormalPictureSerializer(normal_picture)


