WORK_SCHEDULE = (
    ("full-time", "Полный рабочий день"),
    ("part-time", "Частичная занятость"),
    ("remote", "Удаленная работа"),
)

LEVELS_REQUIREMENTS = (
    ("intern", "Intern"),
    ("junior", "Junior"),
    ("junior_plus", "Junior+"),
    ("middle", "Middle"),
    ("middle_plus", "Middle+"),
    ("senior", "Senior"),
    ("team_lead", "Team Lead"),
)

STATUS_RESPONSES = (
    ("new", "Новый"),
    ("accepted", "Принят"),
    ("interview", "Интервью"),
    ("offered", "Предложение на работу"),
    ("rejected", "Отклонен"),
)

STATUS_VACANCY = (
    ("open", " Открыта"),
    ("archived", "Архив"),
)

STATUS_INTERVIEW = (
    ("new", "Создан"),
    ("finished", "Окончен"),
    ("canceled", "Отменен"),
    ("accepted", "Успешен"),
    ("rejected", "Отклонен"),
)

CATEGORY_TYPES = (
    ("backend", "Бэкенд"),
    ("frontend", "Фронтенд"),
    ("fullstack", "Фулстайк"),
    ("analytics", "Аналитика"),
    ("devops", "DevOps"),
    ("design", "Дизайн"),
    ("other", "Другое"),
)

TYPE_SUBJECT = (
        ("question", "Вопрос"),
        ("suggestion", "Предложение"),
        ("complaint", "Жалоба"),
    )
TYPE_NOTIFICATION = (
    ("new_vacancy", "Новая вакансия"),
    ("new_interview", "Новое интервью"),
    ("new_message", "Новое сообщение"),
    ("new_response", "Новый отклик"),
    ("archive_vacancy", "Вакансия перенесена в архив"),
)


USER_TYPES = (
    ("Company", "Компания"),
    ("Employee", "Работник"),
    ("Admin", "Администратор"),
)
