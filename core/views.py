from .serializers import (
    ResumeSerializer,
    VacancySerializer,
    CategorySerializer,
    CommentSerializer,
    ExperienceSerializer,
    StackSerializer,
)
from drf_spectacular.utils import extend_schema

from .models import Resume, Vacancy, Category, Comment, Experience, Stack
from rest_framework import generics


class ExperienceListView(generics.CreateAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()

    @extend_schema(
        request=ExperienceSerializer,
        responses=ExperienceSerializer,
        summary="Добавление опыта работы",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    @extend_schema(
        responses=CommentSerializer,
        summary="Получение комментария",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        request=CommentSerializer,
        responses=CommentSerializer,
        summary="Обновление комментария",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        request=CommentSerializer,
        responses=CommentSerializer,
        summary="Удаление комментария",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        request=CommentSerializer,
        responses=CommentSerializer,
        summary="Частичное обновление комментария",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    @extend_schema(
        request=CommentSerializer,
        responses=CommentSerializer,
        summary="Добавление комментария",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        responses=CommentSerializer,
        summary="Получение комментариев",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @extend_schema(
        responses=CategorySerializer,
        summary="Получение категории",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ResumeListView(generics.ListCreateAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()

    @extend_schema(
        request=ResumeSerializer,
        responses=ResumeSerializer,
        summary="Добавление резюме",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        responses=ResumeSerializer,
        summary="Получение всех резюме",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()

    @extend_schema(
        responses=ResumeSerializer,
        summary="Получение резюме",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        request=ResumeSerializer,
        responses=ResumeSerializer,
        summary="Обновление резюме",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        request=ResumeSerializer,
        responses=ResumeSerializer,
        summary="Удаление резюме",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        request=ResumeSerializer,
        responses=ResumeSerializer,
        summary="Частичное обновление резюме",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class VacancyListView(generics.ListCreateAPIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

    @extend_schema(
        request=VacancySerializer,
        responses=VacancySerializer,
        summary="Добавление вакансии",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        responses=VacancySerializer,
        summary="Получение всех вакансий",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

    @extend_schema(
        responses=VacancySerializer,
        summary="Получение вакансии",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        request=VacancySerializer,
        responses=VacancySerializer,
        summary="Обновление вакансии",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        request=VacancySerializer,
        responses=VacancySerializer,
        summary="Удаление вакансии",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        request=VacancySerializer,
        responses=VacancySerializer,
        summary="Частичное обновление вакансии",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class StackListView(generics.ListAPIView):
    serializer_class = StackSerializer
    queryset = Stack.objects.all()

    @extend_schema(
        responses=StackSerializer,
        summary="Получение всех стеков",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
