from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import Employee, Experience, Resume, Project

from .serializers import (
    EmployeeSerializer,
    ExperienceSerializer,
    ResumeListCreateSerializer,
    ResumeSerializer,
    ProjectSerializer
)


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


class ResumeListView(generics.ListCreateAPIView):
    serializer_class = ResumeSerializer
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
        serializer = self.get_serializer(data=data, context={"request": request})
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


class ProjectListView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    @extend_schema(
        tags=["Проекты"],
        request=ProjectSerializer,
        responses=ProjectSerializer,
        summary="Добавление проекта",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    @extend_schema(
        tags=["Проекты"],
        responses=ProjectSerializer,
        summary="Получение всех проектов",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def create(self, request, *args, **kwargs): 
        employee = request.user.employee
        data = request.data
        serializer = self.get_serializer(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save(employee=employee)

        return Response(serializer.data, status=201)
    

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    @extend_schema(
        tags=["Проекты"],
        responses=ProjectSerializer,
        summary="Получение проекта по id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Проекты"],
        request=ProjectSerializer,
        responses=ProjectSerializer,
        summary="Обновление проекта по id",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Проекты"],
        request=ProjectSerializer,
        responses=ProjectSerializer,
        summary="Удаление проекта по id",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        tags=["Проекты"],
        request=ProjectSerializer,
        responses=ProjectSerializer,
        summary="Частичное обновление проекта по id",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)