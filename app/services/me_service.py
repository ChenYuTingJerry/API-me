from app.model.picture import NormalPicture
from app.model.user import User, UserOtherUserBlockShip


async def get_block_users(user_id: int, limit: int, offset: int) -> list:
    result = (
        await User.load(
            User.id,
            User.name,
            User.gender,
            User.age,
            block_ship=UserOtherUserBlockShip.load(
                UserOtherUserBlockShip.user_id,
                UserOtherUserBlockShip.other_user_id,
            ).on(User.id == UserOtherUserBlockShip.other_user_id),
            picture=NormalPicture.load(
                NormalPicture.asset, NormalPicture.id
            ).on(NormalPicture.id == User.profile_picture_id),
        )
        .where(UserOtherUserBlockShip.user_id == user_id)
        .limit(limit)
        .offset(offset)
        .gino.all()
    )

    return result


async def create_block_user(user_id: int, blocked_user_id: int):
    blocked_user = (
        await UserOtherUserBlockShip.query.where(
            UserOtherUserBlockShip.user_id == user_id
        )
        .where(UserOtherUserBlockShip.other_user_id == blocked_user_id)
        .gino.first()
    )

    if not blocked_user:
        await UserOtherUserBlockShip.create(
            user_id=user_id, other_user_id=blocked_user_id
        )


async def remove_block_user(user_id: int, blocked_user_id: int):
    await UserOtherUserBlockShip.delete.where(
        UserOtherUserBlockShip.other_user_id == blocked_user_id
    ).where(UserOtherUserBlockShip.user_id == user_id).gino.status()
