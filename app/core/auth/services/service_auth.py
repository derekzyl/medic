

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.users.models.model_user import UserModel
from app.core.users.services.service_user import UserService
from app.core.users.types.type_user import CreateUserT, UserT
from app.utils.crud.service_crud import CrudService
from app.utils.crud.types_crud import response_message


class AuthService(UserService):
    def __init__(self, db:AsyncSession) -> None:
        super().__init__(db)
        self.crud_service = CrudService(db=db, model=UserModel) # type: ignore
        self.db = db

    async def create(self, data:CreateUserT):
        user = await self.create_user(data=data)
        if user["data"] is None: # type: ignore
            raise HTTPException(status_code=400, detail=response_message(error="user not created", success_status=False, message="User not created")) 
        
        db_user = UserT(**user["data"]) # type: ignore
        
    def login(self, data:dict):
        pass
    def reset_password(self, data:dict):
        pass
    def change_password(self, data:dict):
        pass
    def logout(self, data:dict):
        pass
    def verify_email(self, data:dict):
        pass
    def forgot_password(self, data:dict):
        
        pass

        