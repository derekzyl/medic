import math
import random
from datetime import datetime, timedelta
from typing import TypedDict

from fastapi import HTTPException
from sqlalchemy import insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import env
from app.config.config import TokenType
from app.config.database import db
from app.core.auth.models.model_token import TokenModel
from app.core.users.types.type_user import UserT
from app.utils.crud.types_crud import response_message
from app.utils.my_jwt import MyJwt

jwt = MyJwt()

def generate_token (user_id:str, token_type:str ,expires_in:int) -> str:
    return jwt.create_token(subject=user_id,token_type=token_type, expires_in=expires_in)


def generate_otp_token(otp_length:int=6) -> int:
    otp:int = math.floor(random.random() * (10 ** otp_length))
    return otp

    

class saveToken(TypedDict):
    token:str
    expires_in:int
    type:TokenType
    user_id:str
    blacklisted:bool
 

async def save_token(data:saveToken, db:AsyncSession):
    token_data = TokenModel(**data)
    db.add(token_data)
    await db.commit()
    await db.refresh(token_data)
    return token_data

async def verify_token(token:str, type:TokenType, db:AsyncSession):
    token_data = jwt.verify_token(token=token)
    
    if isinstance(token_data['sub'], str)==False:
        raise HTTPException(
            status_code=400,
                            detail=response_message(error="Invalid token", success_status=False, message="Invalid token")
        )
    try:
        token_data = await db.get_one(TokenModel, {
            "user_id": token_data['sub'],
            
            "type": type,
            "blacklisted": False
            })

        stmt =(update(TokenModel).values(blacklisted=True).where(TokenModel.id == token_data.id))
        await db.execute(stmt)
        if token_data is None:
            raise HTTPException(
                status_code=400,
                                detail=response_message(error="Invalid token", success_status=False, message="Invalid token")
            )
        return token_data    
    except Exception as e:
        raise HTTPException(
            status_code=400,
                            detail=response_message(error=e, success_status=False, message="Invalid token")
        )    
    
async def verify_otp_token(token:str, user_id:str, type:TokenType, db:AsyncSession):
    try:
        token_data = await db.get_one(TokenModel, {
            "user_id": user_id,
            "type": type,
            "blacklisted": False,
            "token":token
            })
        # update
        stmt =(update(TokenModel).values(blacklisted=True).where(TokenModel.id == token_data.id))
        await db.execute(stmt)
        if token_data is None:
            raise HTTPException(
                status_code=400,
                                detail=response_message(error="Invalid token", success_status=False, message="Invalid token")
            )
        return token_data
    except Exception as e:
        raise HTTPException(
            status_code=400,
                            detail=response_message(error=e, success_status=False, message="Invalid token")
        )
    



async def generate_auth_token(user:UserT,db:AsyncSession):
    access_expiry_time = env.env['jwt']['jwt_access_expiry_time']
    refresh_expiry_time = env.env['jwt']['jwt_refresh_expiry_time']

    access_token = MyJwt().create_token(subject=user['id'], token_type=TokenType.ACCESS_TOKEN, expires_in=access_expiry_time)
    refresh_token = MyJwt().create_token(subject=user['id'], token_type=TokenType.REFRESH_TOKEN, expires_in=refresh_expiry_time)

    await save_token(data={
        "token":refresh_token,
        "expires_in":access_expiry_time,
        "type":TokenType.REFRESH_TOKEN,
        "user_id":user['id'],
        "blacklisted":False
    }, db=db)

    return {
       "access":{"token":access_token, "expires":datetime.now()+  timedelta(minutes=access_expiry_time)},
       "refresh":{"token":refresh_token, "expires":datetime.now()+ timedelta(minutes=refresh_expiry_time)}
    }
    
    

    
    
    
def generate_reset_password_token():
    pass
def generate_login_token():
    pass