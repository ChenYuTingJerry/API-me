from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    Boolean,
    Float,
    Date,
    ForeignKey,
)

from app.db import pg


class User(pg.Model):
    __tablename__ = "users"

    id = pg.Schema.Column(Integer, primary_key=True)
    name = pg.Schema.Column(String)
    udid = pg.Schema.Column(pg.Schema.String)
    sip_user_id = pg.Schema.Column(Integer)
    phone = pg.Schema.Column(pg.Schema.String)
    gender = pg.Schema.Column(Boolean)
    orientation = pg.Schema.Column(Integer)
    age = pg.Schema.Column(Integer)
    favor_age_min = pg.Schema.Column(Integer)
    favor_age_max = pg.Schema.Column(Integer)
    lat = pg.Schema.Column(Float)
    lon = pg.Schema.Column(Float)
    locale = pg.Schema.Column(String)
    last_login = pg.Schema.Column(DateTime)
    is_angel = pg.Schema.Column(Boolean, default=False)
    head_id = pg.Schema.Column(Integer)
    be_night = pg.Schema.Column(Boolean, default=False)
    unread_count = pg.Schema.Column(Integer, default=0)
    email = pg.Schema.Column(String)
    encrypted_password = pg.Schema.Column(String)
    reset_password_token = pg.Schema.Column(String)
    reset_password_sent_at = pg.Schema.Column(DateTime)
    remember_created_at = pg.Schema.Column(DateTime)
    sign_in_count = pg.Schema.Column(Integer, nullable=False, default=0)
    current_sign_in_at = pg.Schema.Column(DateTime)
    last_sign_in_at = pg.Schema.Column(DateTime)
    current_sign_in_ip = pg.Schema.Column(String)
    last_sign_in_ip = pg.Schema.Column(String)
    code_push_key = pg.Schema.Column(String)
    block_ids = pg.Schema.Column(String)
    interest_ids = pg.Schema.Column(String)
    interest_texts = pg.Schema.Column(String)
    favor_distance = pg.Schema.Column(Integer, default=0)
    birthday = pg.Schema.Column(DateTime)
    blocked = pg.Schema.Column(Boolean, default=False)
    picture_id = pg.Schema.Column(Integer)
    crown = pg.Schema.Column(Boolean, default=False)
    playing = pg.Schema.Column(Boolean, default=False)
    pin = pg.Schema.Column(String)
    languages = pg.Schema.Column(String)
    favor_languages = pg.Schema.Column(String)
    stored_data = pg.Schema.Column(String)
    coin = pg.Schema.Column(Integer, default=0)
    membership_id = pg.Schema.Column(Integer)
    membership_expires_at = pg.Schema.Column(DateTime)
    daily_coin_added_at = pg.Schema.Column(DateTime)
    profession_id = pg.Schema.Column(Integer)
    profession_at = pg.Schema.Column(DateTime)
    online = pg.Schema.Column(Boolean, default=False)
    earning = pg.Schema.Column(Integer, default=0)
    profile_picture_id = pg.Schema.Column(Integer)
    picture_array = pg.Schema.Column(String)
    voice_id = pg.Schema.Column(Integer)
    created_channel_at = pg.Schema.Column(DateTime)
    channel_title = pg.Schema.Column(String)
    price = pg.Schema.Column(Integer)
    viewed_count = pg.Schema.Column(Integer, default=0)
    call_count = pg.Schema.Column(Integer, default=0)
    pro_blocked = pg.Schema.Column(Boolean, default=False)
    role = pg.Schema.Column(Integer, default=0)
    call = pg.Schema.Column(String)
    pro_blocked_at = pg.Schema.Column(DateTime)
    account_kit_user_id = pg.Schema.Column(Integer)
    account_kit_access_token = pg.Schema.Column(String)
    account_kit_user_info = pg.Schema.Column(String)
    account_kit_phone = pg.Schema.Column(String)
    notification_unread_count = pg.Schema.Column(Integer, default=0)
    pro_call_muted_until = pg.Schema.Column(DateTime)
    pro_boosted_until = pg.Schema.Column(DateTime)
    google_sub = pg.Schema.Column(String)
    google_email = pg.Schema.Column(String)
    google_auth_payload = pg.Schema.Column(String)
    ichi_open_id = pg.Schema.Column(Integer)
    ichi_user_id = pg.Schema.Column(Integer)
    ichi_user_info = pg.Schema.Column(String)
    unanswer_pro_calls_count = pg.Schema.Column(Integer, default=0)
    last_device_info = pg.Schema.Column(String)
    country_code = pg.Schema.Column(String)
    last_appsflyer_info = pg.Schema.Column(String)
    forum_blocked_at = pg.Schema.Column(DateTime)
    forum_blocked = pg.Schema.Column(Boolean, default=False)
    abilities = pg.Schema.Column(Integer)
    free_trials_redeemed = pg.Schema.Column(Integer)
    email_confirmed_at = pg.Schema.Column(DateTime)
    email_confirmation_sent_at = pg.Schema.Column(DateTime)
    school_email = pg.Schema.Column(String)
    school_name = pg.Schema.Column(String)
    school_email_confirmed_at = pg.Schema.Column(DateTime)
    school_email_confirmation_sent_at = pg.Schema.Column(DateTime)
    intro = pg.Schema.Column(String)
    safe_mode = pg.Schema.Column(Boolean)
    likes_count = pg.Schema.Column(Integer)
    firebase_phone_auth_local_id = pg.Schema.Column(String)
    firebase_phone_auth_phone = pg.Schema.Column(String)
    zuvio_user_id = pg.Schema.Column(String)
    zuvio_school_name = pg.Schema.Column(String)
    zuvio_email = pg.Schema.Column(String)
    event_notif_unread_count = pg.Schema.Column(Integer)
    deleted_at = pg.Schema.Column(DateTime)
    vip_coin = pg.Schema.Column(Integer)
    vip_coin_expires_at = pg.Schema.Column(DateTime)
    payment_email = pg.Schema.Column(String)
    fb_uid = pg.Schema.Column(String)
    fb_email = pg.Schema.Column(String)
    fb_token = pg.Schema.Column(String)
    fb_authed_at = pg.Schema.Column(DateTime)
    is_migrated_from_sms = pg.Schema.Column(Boolean)
    g_exp = pg.Schema.Column(Integer)
    followers_count = pg.Schema.Column(Integer)
    apple_email = pg.Schema.Column(String)
    info_motified_at = pg.Schema.Column(Date)
    updated_at = pg.Schema.Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = pg.Schema.Column(DateTime, default=datetime.utcnow)

    @property
    def v_level(self):
        return self.vip_coin if self.vip_coin else 0


class UserOtherUserBlockShip(pg.Model):
    __tablename__ = "user_other_user_block_ships"

    id = pg.Schema.Column(Integer, primary_key=True)
    user_id = pg.Schema.Column(ForeignKey("users.id"))
    other_user_id = pg.Schema.Column(ForeignKey("users.id"))
    updated_at = pg.Schema.Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = pg.Schema.Column(DateTime, default=datetime.utcnow)
