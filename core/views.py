from .serializers import (
    ResumeListCreateSerializer,
    ResumeSerializer,
    VacancyListCreateSerializer,
    VacancySerializer,
    CategorySerializer,
    CommentSerializer,
    ExperienceSerializer,
    StackSerializer,
    FavoriteResumeSerializer,
    FavoriteVacancySerializer,
    CompanySerializer,
    EmployeeSerializer,
)
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from .models import (
    Company,
    Employee,
    Resume,
    Vacancy,
    Category,
    Comment,
    Experience,
    Stack,
    FavoriteResume,
    FavoriteVacancy,
)
from rest_framework import generics


class EmployeeListView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    @extend_schema(
        tags=["Работники"],
        request=EmployeeSerializer,
        responses=EmployeeSerializer,
        summary="Добавление работника",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        tags=["Работники"],
        responses=EmployeeSerializer,
        summary="Получение всех работников",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    @extend_schema(
        tags=["Работники"],
        responses=EmployeeSerializer,
        summary="Получение работника по id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Работники"],
        request=EmployeeSerializer,
        responses=EmployeeSerializer,
        summary="Обновление работника по id",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Работники"],
        request=EmployeeSerializer,
        responses=EmployeeSerializer,
        summary="Удаление работника по id",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        tags=["Работники"],
        request=EmployeeSerializer,
        responses=EmployeeSerializer,
        summary="Частичное обновление работника по id",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


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


class ExperienceListView(generics.CreateAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()

    @extend_schema(
        tags=["Опыт работы"],
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
        serializer = self.get_serializer(
            data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

    @extend_schema(
        tags=["Комментарии"],
        responses=CommentSerializer,
        summary="Получение всех комментариев",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @extend_schema(
        tags=["Категории"],
        responses=CategorySerializer,
        summary="Получение категории",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ResumeListView(generics.ListCreateAPIView):
    serializer_class = ResumeListCreateSerializer
    queryset = Resume.objects.all()

    @extend_schema(
        tags=["Резюме"],
        request=ResumeListCreateSerializer,
        responses=ResumeListCreateSerializer,
        summary="Добавление резюме",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        tags=["Резюме"],
        responses=ResumeListCreateSerializer,
        summary="Получение всех резюме",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        employee = request.user.employee
        data = request.data
        serializer = self.get_serializer(
            data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(employee=employee)

        return Response(serializer.data, status=201)
class ResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()

    @extend_schema(
        tags=["Резюме"],
        responses=ResumeSerializer,
        summary="Получение резюме по id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Резюме"],
        request=ResumeSerializer,
        responses=ResumeSerializer,
        summary="Обновление резюме по id",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Резюме"],
        request=ResumeSerializer,
        responses=ResumeSerializer,
        summary="Удаление резюме по id",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        tags=["Резюме"],
        request=ResumeSerializer,
        responses=ResumeSerializer,
        summary="Частичное обновление резюме по id",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


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
        serializer = self.get_serializer(
            data=data, context={'request': request})
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


class StackListView(generics.ListAPIView):
    serializer_class = StackSerializer
    queryset = Stack.objects.all()

    @extend_schema(
        tags=["Стеки"],
        responses=StackSerializer,
        summary="Получение всех стеков",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


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
        serializer = self.get_serializer(
            data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(company=company)

        return Response(serializer.data, status=201)
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
        serializer = self.get_serializer(
            data=data, context={'request': request})
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
