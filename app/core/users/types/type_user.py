
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import NotRequired, Optional, TypedDict


@dataclass
class UserD:
    id: str

    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    language: str 
    remember_token: str
    deleted_at: datetime
    created_at: datetime 
    updated_at: datetime 
    is_commission_agent: bool
    commission_agent_id: str
    businessId: Optional[int]
    allow_login: bool
    user_type:str
    gender:str


class UserT(TypedDict, ):
    id: str

    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    language: str

    signup_type: str # Either 'email' or 'phone' GOOGLE or FACEBOOK
    remember_token: str
    deleted_at: datetime
    created_at: datetime 
    updated_at: datetime 
    is_commission_agent: bool
    commission_agent_id: str
    businessId: int
    allow_login: bool
    user_type:str
    gender:str
class CreateUserT(TypedDict ):


    first_name: str
    last_name: str
    username: NotRequired[str]
    email: str
    password: str
    language: NotRequired[str]

    signup_type: str # Either 'email' or 'phone' GOOGLE or FACEBOOK
    remember_token: NotRequired[str]
    deleted_at: NotRequired[datetime]
    created_at: NotRequired[datetime] 
    updated_at: NotRequired[datetime] 
    is_commission_agent: bool
    commission_agent_id: NotRequired[str]
    businessId: NotRequired[int]
    allow_login: NotRequired[bool]
    user_type:NotRequired[str]
    gender:NotRequired[str]

    
class UpdateUserT(TypedDict ):
    first_name: str
    last_name: str
    username: NotRequired[str]

    language: NotRequired[str]
    remember_token: NotRequired[str]

    gender:NotRequired[str]

    
class GenderE(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class UserTypeE(Enum):
    CUSTOMER = "customer"
    BUSINESS = "business"
    AGENT = "agent"
    STAFF='STAFF'
    API_USER='API_USER'
    SUPER_ADMIN = "super_admin"
    COMMISSION_AGENT= "commission_agent"