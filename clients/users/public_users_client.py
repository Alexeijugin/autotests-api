from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient

class UserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя
    """
    email: str
    password: str
    lastname: str
    firstname: str
    middleName: str
class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: UserRequestDict) -> Response:
        """
        Метод выполняет создание пользователя

        :param request: Словарь с email, password, lastname, firstname, middleName
        :return:  Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)