

from sqlalchemy import Mapped
from sqlalchemy.orm import mapped_column

from app.config.database.db import Base
from app.utils.generate_id import generate_id


class UserModel(Base):
    id:Mapped[str] = mapped_column(primary_key=True, default=generate_id())
    username: Mapped[str]
    password: Mapped[str]
    email:Mapped[str]