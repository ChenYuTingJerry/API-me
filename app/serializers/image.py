import os
from dataclasses import dataclass

from app.model.picture import NormalPicture
from app.serializers import Serializer
from app.utils.descriptor import String
from config import config


class PictureUrlSerializer(Serializer):
    url: String

    def __init__(self, file_name):
        self.url = file_name

    @property
    def pic_storage(self):
        return f"http://{config.HOST}:{config.PORT}"


class PictureSerializer(Serializer):
    normal: PictureUrlSerializer
    medium: PictureUrlSerializer
    thumb: PictureUrlSerializer

    def __init__(self, pic_type, category, asset_id, asset_name):
        if os.getenv("ENV") == "prod":
            pass
        else:
            prefix = f"http://{config.HOST}:{config.PORT}/uploads/{pic_type}/{category}/{asset_id}"
        self.normal = PictureUrlSerializer(f"{prefix}/normal_{asset_name}")
        self.medium = PictureUrlSerializer(f"{prefix}/medium_{asset_name}")
        self.thumb = PictureUrlSerializer(f"{prefix}/thumb_{asset_name}")


class NormalPictureSerializer(Serializer):
    asset: PictureSerializer
    url: String

    def __init__(self, normal_picture: NormalPicture):
        pic_type = "normal_picture"
        category = "asset"
        if os.getenv("ENV") == "prod":
            pass
        else:
            self.url = f"http://{config.HOST}:{config.PORT}" \
                       f"/uploads/{pic_type}/{category}/{normal_picture.id}/{normal_picture.asset}"
            self.asset = PictureSerializer(
                pic_type, category, normal_picture.id, normal_picture.asset
            )
