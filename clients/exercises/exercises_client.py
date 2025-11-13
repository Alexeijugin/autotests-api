from clients.api_client import APIClient

from httpx import Response
from typing import TypedDict

class GetExercisesQueryDict():
    """
    Описание структуры запроса на получение списка заданий
    """
    courseId: str

class CreatEexerciseRequestDict():
    """
    Описание структуры запроса на получение задания
    """
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None


class UpdateExerciseRequestDict():
    """
    Описание структуры запроса на обновление задания
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка заданий

        :param query: Индефикаторы списка заданий
        :return: Ответ от сервера в виде обьекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Индефикатор задания
        :return: Ответ от сервера в виде обьекта httpx.Response
        """
        return self.get(f"/api/v1/exercises{exercise_id}")

    def create_exercise_api(self, request: CreatEexerciseRequestDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде обьекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Индефикатор задания
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде обьекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.
        :param exercise_id: Индефикатор задания
        :return: Ответ от сервера в виде обьекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises{exercise_id}')