from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import Comment, Company, Vacancy

from .serializers import (
    CommentSerializer,
    CompanySerializer,
    VacancyListCreateSerializer,
    VacancySerializer,
)


class CompanyListView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    @extend_schema(
        tags=["Компании"],
        request=CompanySerializer,
        responses=CompanySerializer,
        summary="Добавление компании",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        tags=["Компании"],
        responses=CompanySerializer,
        summary="Получение всех компаний",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    @extend_schema(
        tags=["Компании"],
        responses=CompanySerializer,
        summary="Получение компании по id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Компании"],
        request=CompanySerializer,
        responses=CompanySerializer,
        summary="Обновление компании по id",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Компании"],
        responses=CompanySerializer,
        summary="Удаление компании по id",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        tags=["Компании"],
        request=CompanySerializer,
        responses=CompanySerializer,
        summary="Частичное обновление компании по id",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    @extend_schema(
        tags=["Комментарии"],
        responses=CommentSerializer,
        summary="Получение комментария по id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Комментарии"],
        request=CommentSerializer,
        responses=CommentSerializer,
        summary="Обновление комментария по id",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Комментарии"],
        request=CommentSerializer,
        responses=CommentSerializer,
        summary="Удаление комментария по id",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        tags=["Комментарии"],
        request=CommentSerializer,
        responses=CommentSerializer,
        summary="Частичное обновление комментария по id",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    @extend_schema(
        tags=["Комментарии"],
        request=CommentSerializer,
        responses=CommentSerializer,
        summary="Добавление комментария",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        serializer = self.get_serializer(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

    @extend_schema(
        tags=["Комментарии"],
        responses=CommentSerializer,
        summary="Получение всех комментариев",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class VacancyListView(generics.ListCreateAPIView):
    serializer_class = VacancyListCreateSerializer
    queryset = Vacancy.objects.all()

    @extend_schema(
        tags=["Вакансии"],
        request=VacancyListCreateSerializer,
        responses=VacancyListCreateSerializer,
        summary="Добавление вакансии",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        tags=["Вакансии"],
        responses=VacancyListCreateSerializer,
        summary="Получение всех вакансий",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        company = request.user.company
        data = request.data
        serializer = self.get_serializer(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save(company=company)

        return Response(serializer.data, status=201)


class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

    @extend_schema(
        tags=["Вакансии"],
        responses=VacancySerializer,
        summary="Получение вакансии по id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Вакансии"],
        request=VacancySerializer,
        responses=VacancySerializer,
        summary="Обновление вакансии по id",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Вакансии"],
        request=VacancySerializer,
        responses=VacancySerializer,
        summary="Удаление вакансии по id",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        tags=["Вакансии"],
        request=VacancySerializer,
        responses=VacancySerializer,
        summary="Частичное обновление вакансии по id",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
