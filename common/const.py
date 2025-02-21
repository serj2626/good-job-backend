WORK_SCHEDULE = (
    ("full-time", "Полный рабочий день"),
    ("part-time", "Частичная занятость"),
    ("project", "Проектная работа"),
)

FORMAT_WORK = (
    ("office", "В офисе"),
    ("remote", "Удаленная работа"),
    ("hybrid", "Гибридная работа"),
)


LEVELS_REQUIREMENTS = (
    ("none", "Не имеет значения"),
    ("intern", "Стажер"),
    ("junior", "Junior"),
    ("junior_plus", "Junior+"),
    ("middle", "Middle"),
    ("middle_plus", "Middle+"),
    ("senior", "Senior"),
    ("team_lead", "Team Lead"),
)

STATUS_RESPONSES = (
    ("new", "Новый"),
    ("accepted", "Приглашение"),
    ("interview", "Интервью"),
    ("offered", "Предложение на работу"),
    ("rejected", "Отклонен"),
)

STATUS_VACANCY = (
    ("open", " Открыта"),
    ("archived", "В архиве"),
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

TYPE_FEEDBACK = (
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
    ("new_user", "На вас подписался новый пользователь"),
    ("new_visitor", "Вашу страницу посетил новый пользователь"),
)


USER_TYPES = (
    ("Company", "Компания"),
    ("Employee", "Специалист"),
    ("Admin", "Администратор"),
)


TYPE_SOCIAL_LINK = (
    ("vk", "Вконтакте"),
    ("linkedin", "LinkedIn"),
    ("tg", "Telegram"),
    ("github", "GitHub"),
    ("gitlab", "GitLab"),
    ("habr", "Habr"),
    ("other", "Другое"),
)

STATUS_EMPLOYEE = (
    ("unemployed", "Не ищу работу"),
    ("search", "В поиске работы"),
)

STATUS_FRIEND_REQUEST = (
    ("pending", "Отправлена"),
    ("accepted", "Принята"),
    ("rejected", "Отклонена"),
)

TYPE_EDUCATION = (
    ("univer", "Высшее образование"),
    ("course", "Курсы"),
    ("other", "Другое"),
)

TYPE_GENDER = (("male", "Мужской"), ("female", "Женский"), ("other", "Не указано"))


CURRENCY_TYPE = (
    ("RUB", "RUB"),
    ("USD", "USD"),
    ("EUR", "EUR"),
)

COMPANY_TYPES = (
    ("OOO", "ООО"),
    ("IP", "ИП"),
    ("UP", "УП"),
    ("PAO", "ПАО"),
    ("Corp", "Corp"),
    ("ZAO", "ЗАО"),
    ("OAO", "ОАО"),
    ("AO", "АО"),
    ("other", "Другое"),
)

STATUS_CHECK_COMPANY = (
    ("sent", "Отправлено"),
    ("pending", "На расмотрении"),
    ("accepted", "Принято"),
    ("rejected", "Отклонено"),
)


MONTHS = (
    (1, "Январь"),
    (2, "Февраль"),
    (3, "Март"),
    (4, "Апрель"),
    (5, "Май"),
    (6, "Июнь"),
    (7, "Июль"),
    (8, "Август"),
    (9, "Сентябрь"),
    (10, "Октябрь"),
    (11, "Ноябрь"),
    (12, "Декабрь"),
)
