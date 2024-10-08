from pydantic import BaseModel 
import datetime

class CrearUsuario(BaseModel):
    nombre: str
    apellido: str
    email: str
    password: str

class RequestDetails(BaseModel):
    email:str
    password:str
        
class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class ChangePassword(BaseModel):
    email:str
    old_password:str
    new_password:str

class TokenCreate(BaseModel):
    user_id:str
    access_token:str
    refresh_token:str
    status:bool
    created_date:datetime.datetime

class UpdateUser(BaseModel):
    nombre: str
    apellido: str
    email: str
    password: str

class CreatePermission(BaseModel):
    name: str
    description: str = None

class UpdatePermission(BaseModel):
    name: str = None
    description: str = None


class PermissionSchema(BaseModel):
    id: int
    name: str
    description: str = None

    class Config:
        orm_mode = True
        from_attributes = True

class PasswordResetRequest(BaseModel):
    email: str

class PasswordResetVerify(BaseModel):
    email: str
    token: str
    new_password: str
