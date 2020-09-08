import io
from abc import ABC, abstractmethod
from importlib import import_module

from PIL import Image

from app.utils.converter import StringConvert


class ImageInterface(ABC):
    @abstractmethod
    async def save(self, path):
        return NotImplemented


class OriginalImage(ImageInterface):
    def __init__(self, image_data):
        self.image = Image.open(io.BytesIO(image_data))

    async def save(self, path):
        self.image.save(path)


class NormalImage(ImageInterface):
    def __init__(self, image_data):
        self.image = Image.open(io.BytesIO(image_data))
        self.image = self.image.resize((800, 800))

    async def save(self, path):
        self.image.save(path)


class ThumbImage(ImageInterface):
    def __init__(self, image_data):
        self.image = Image.open(io.BytesIO(image_data))
        self.image = self.image.resize((120, 120))

    async def save(self, path):
        self.image.save(path)


class MediumImage(ImageInterface):
    def __init__(self, image_data):
        self.image = Image.open(io.BytesIO(image_data))
        self.image = self.image.resize((360, 360))

    async def save(self, path):
        self.image.save(path)


class ImageFactory:
    @staticmethod
    def get_instance(category):
        module = import_module("app.utils.image")
        class_name = f"{StringConvert.to_upper_camel_case(category)}Image"
        return getattr(module, class_name)
