from pydantic import BaseModel, EmailStr, Field


# class UserBase(BaseModel):
#     """
#     Создание базовой структуры
#     """
#     email: EmailStr
#     last_name: str = Field(alias="lastName")
#     first_name: str = Field(alias="firstName")
#     middle_name: str = Field(alias="middleName")
#
# class UserSchema(UserBase):
#     """
#     Модель для данных пользователя
#     """
#     id: int
#
#
# class CreateUserRequestSchema(UserBase):
#     """
#     Модель для запроса на создание пользователя
#     """
#     password: str
#
#
# class CreateUserResponseSchema(BaseModel):
#     user: UserSchema

class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema