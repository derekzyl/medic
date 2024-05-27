
from typing import TYPE_CHECKING

from sqlalchemy import (ARRAY, DATETIME, ENUM, INTEGER, Boolean, DateTime,
                        Enum, Float, ForeignKey, Integer, String)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database.db import Base, TimeStamp
from app.core.users.types.type_user import GenderE, UserTypeE
from app.utils.uuid_generator import id_gen

if TYPE_CHECKING:
    from app.core.auth.models.model_token import TokenModel


class UserModel(Base, TimeStamp):
    __tablename__ = "USER"
    id:Mapped[str] = mapped_column(
        String(255), primary_key=True, default=id_gen() , unique=True
    )
    first_name:Mapped[str]
    last_name:Mapped[str]
    password:Mapped[str] =mapped_column(String(255), nullable=False)
    email:Mapped[str]= mapped_column(String(255), unique=True, nullable=False)
    phone:Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    language:Mapped[str]
    deleted_at:Mapped[DateTime]
    gender:Mapped[str]=mapped_column(Enum(GenderE))
    user_type:Mapped[str] = mapped_column(Enum(UserTypeE))
    allow_login:Mapped[bool] = mapped_column(Boolean, default=True)
    is_commission_agent:Mapped[bool] = mapped_column(Boolean, default=False)


    #relationship
   
    user__token:Mapped["TokenModel"] = relationship(back_populates="token__user")


