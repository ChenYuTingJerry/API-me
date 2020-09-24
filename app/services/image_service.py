import hashlib
from pathlib import Path

from sanic.request import File

from app.model.picture import NormalPicture
from app.utils.image import ImageFactory
from config import config


async def save_normal_picture(image: File, user_id: int):
    # 1. Create initial Picture model for getting new id
    p = await NormalPicture.create(user_id=user_id)

    # 2. Generate store directories and saves pics
    categories = ("original", "normal", "medium", "thumb")
    store_dir = f"{config.NORMAL_PICTURE_PATH}/{p.id}"
    Path(store_dir).mkdir(parents=True, exist_ok=True)
    md5 = hashlib.md5(store_dir.encode()).hexdigest()
    file_extension = image.type[image.type.index("/") + 1:]
    file_name = f"{md5}-v2.{file_extension}"
    await _save_images_by_categories(
        categories, store_dir, file_name, image.body
    )
    await p.update(asset=file_name).apply()


async def _save_images_by_categories(
    categories: tuple, store_dir: str, file_name: str, image_body: bytes
):
    result = {}
    for category in categories:
        im = ImageFactory.get_instance(category)(image_body)
        result[category] = (
            f"{category}_{file_name}" if category != "original" else file_name
        )
        await im.save(f"{store_dir}/{result[category]}")
    return result
