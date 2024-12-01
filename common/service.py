def get_clear_slug(email: str) -> str:
    """
    Функция возвращает чистый slug без домена

    :param email: email
    :return: clear slug
    """
    indx = email.find("@")
    return email[:indx]


def get_path_for_avatar(instance, filename) -> str:
    """
    Функция возвращает путь к аватару

    :param instance: user
    :param filename: filename
    :return: path
    """

    return f"resumes/{instance.employee.user.email}/{instance.id}/{filename}"


def get_path_for_avatar_employee(instance, filename) -> str:
    """
    Функция возвращает путь к аватару работника

    :param instance: employee
    :param filename: filename
    :return: path
    """

    return f"employees/{instance.user.email}/{filename}"


def get_path_for_avatar_company(instance, filename) -> str:
    """
    Функция возвращает путь к аватару компании

    :param instance: company
    :param filename: filename
    :return: path
    """

    return f"company/{instance.user.email}/{instance.name}/{filename}"


def get_path_for_photo_feedback(instance, filename) -> str:
    """
    Функция возвращает путь к фото обратной связи

    :param instance: feedback
    :param filename: filename
    :return: path
    """

    return f"feedback/{instance.user.email}/{instance.id}/{filename}"


def get_path_for_image_project(instance, filename) -> str:
    """
    Функция возвращает путь к фото проекта

    :param instance: project
    :param filename: filename
    :return: path
    """

    return f"projects/{instance.employee.user.email}/{filename}"


def get_path_for_check_company_egrul(instance, filename):
    """
    Функция возвращает путь к выписке из ЕГРЮЛ и ЕГРИП

    :param instance: company
    :param filename: filename
    :return: path
    """
    return f"company/{instance.company.slug}/docs/egrul/{filename}"


def get_path_for_check_company_certificate(instance, filename):
    """
    Функция возвращает путь к Cвидетельство о регистрации фирмы или ИП

    :param instance: company
    :param filename: filename
    :return: path
    """
    return f"company/{instance.company.slug}/docs/certificate/{filename}"


def get_path_for_check_company_certificate_nalog(instance, filename):
    """
    Функция возвращает путь к Cправка о постановке на учет в налоговом органе

    :param instance: company
    :param filename: filename
    :return: path
    """
    return f"company/{instance.company.slug}/docs/certificate_nalog/{filename}"


def get_path_for_check_company_constitution(instance, filename):
    """
    Функция возвращает путь к Устав

    :param instance: company
    :param filename: filename
    :return: path
    """
    return f"company/{instance.company.slug}/docs/constitution/{filename}"


def get_path_for_check_company_license(instance, filename):
    """
    Функция возвращает путь к Лицензия на необходимые виды деятельности

    :param instance: company
    :param filename: filename
    :return: path
    """
    return f"company/{instance.company.slug}/docs/license/{filename}"


def get_path_for_check_company_no_debt(instance, filename):
    """
    Функция возвращает путь к Справка, подтверждающая отсутствие долгов по налогам и другим платежам

    :param instance: company
    :param filename: filename
    :return: path
    """
    return f"company/{instance.company.slug}/docs/no_debt/{filename}"
