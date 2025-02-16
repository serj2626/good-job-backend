from django.db import models

from common.models import MyBaseModel
from companies.models import Company, Vacancy
from employees.models import Employee, Resume


class FavoriteVacancy(MyBaseModel):
    """
    Модель избранных вакансий для работника.
    """

    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, null=True, verbose_name="Вакансия"
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name="Работник"
    )

    def __str__(self):
        return f"Избранная вакансия {self.vacancy} для работника {self.employee}"

    class Meta:
        verbose_name = "Избранные вакансии"
        verbose_name_plural = "Избранные вакансии"


class FavoriteResume(MyBaseModel):
    """
    Модель избранных резюме  для компании.
    """

    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, null=True, verbose_name="Резюме"
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name="Компания"
    )

    def __str__(self):
        return f"Избранное резюме {self.resume} для компании {self.company}"

    class Meta:
        verbose_name = "Избранные резюме"
        verbose_name_plural = "Избранные резюме"
