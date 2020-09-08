from datetime import datetime

from sqlalchemy import Integer, String, DateTime, ForeignKey, func

from app.db import pg


class Picture(pg.Model):
    __tablename__ = "pictures"

    id = pg.Schema.Column(Integer, primary_key=True)
    user_id = pg.Schema.Column(ForeignKey("users.id"))
    clear = pg.Schema.Column(String)
    blur1 = pg.Schema.Column(String)
    blur2 = pg.Schema.Column(String)
    updated_at = pg.Schema.Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = pg.Schema.Column(DateTime, default=datetime.utcnow)


class NormalPicture(pg.Model):
    __tablename__ = "normal_pictures"

    id = pg.Schema.Column(Integer, primary_key=True)
    user_id = pg.Schema.Column(ForeignKey("users.id"))
    asset = pg.Schema.Column(String)
    updated_at = pg.Schema.Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = pg.Schema.Column(DateTime, default=datetime.utcnow)
