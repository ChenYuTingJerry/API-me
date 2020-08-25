from sqlalchemy import Integer, String, DateTime, ForeignKey

from app.db import pg


class ApiToken(pg.Model):
    __tablename__ = "api_tokens"

    id = pg.Schema.Column(Integer, primary_key=True)
    token = pg.Schema.Column(String)
    user_id = pg.Schema.Column(ForeignKey("users.id"))
    expires_at = pg.Schema.Column(DateTime)
    updated_at = pg.Schema.Column(DateTime)
    created_at = pg.Schema.Column(DateTime)
