from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import FavoriteResume, FavoriteVacancy

from .serializers import (
    FavoriteResumeSerializer,
    FavoriteVacancySerializer,
)


class FavoriteVacancyListView(generics.ListCreateAPIView):
    serializer_class = FavoriteVacancySerializer
    queryset = FavoriteVacancy.objects.all()

    @extend_schema(
        tags=["Избранные вакансии"],
        request=FavoriteVacancySerializer,
        responses=FavoriteVacancySerializer,
        summary="Добавление избранной вакансии",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        tags=["Избранные вакансии"],
        responses=FavoriteVacancySerializer,
        summary="Получение всех избранных вакансий",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        employee = request.user.employee
        data = request.data
        serializer = self.get_serializer(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save(employee=employee)


class FavoriteVacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FavoriteVacancySerializer
    queryset = FavoriteVacancy.objects.all()

    @extend_schema(
        tags=["Избранные вакансии"],
        responses=FavoriteVacancySerializer,
        summary="Получение избранной вакансии по id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Избранные вакансии"],
        request=FavoriteVacancySerializer,
        responses=FavoriteVacancySerializer,
        summary="Обновление избранной вакансии по id",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Избранные вакансии"],
        request=FavoriteVacancySerializer,
        responses=FavoriteVacancySerializer,
        summary="Удаление избранной вакансии по id",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        tags=["Избранные вакансии"],
        request=FavoriteVacancySerializer,
        responses=FavoriteVacancySerializer,
        summary="Частичное обновление избранной вакансии по id",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class FavoriteResumeListView(generics.ListCreateAPIView):
    serializer_class = FavoriteResumeSerializer
    queryset = FavoriteResume.objects.all()

    @extend_schema(
        tags=["Избранные резюме"],
        request=FavoriteResumeSerializer,
        responses=FavoriteResumeSerializer,
        summary="Добавление избранного резюме",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        tags=["Избранные резюме"],
        responses=FavoriteResumeSerializer,
        summary="Получение всех избранных резюме",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class FavoriteResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FavoriteResumeSerializer
    queryset = FavoriteResume.objects.all()

    @extend_schema(
        tags=["Избранные резюме"],
        responses=FavoriteResumeSerializer,
        summary="Получение избранного резюме по id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Избранные резюме"],
        request=FavoriteResumeSerializer,
        responses=FavoriteResumeSerializer,
        summary="Обновление избранного резюме по id",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Избранные резюме"],
        request=FavoriteResumeSerializer,
        responses=FavoriteResumeSerializer,
        summary="Удаление избранного резюме по id",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        tags=["Избранные резюме"],
        request=FavoriteResumeSerializer,
        responses=FavoriteResumeSerializer,
        summary="Частичное обновление избранного резюме по id",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        company = request.user.company
        data = request.data
        serializer = self.get_serializer(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save(company=company)

        return Response(serializer.data, status=201)
