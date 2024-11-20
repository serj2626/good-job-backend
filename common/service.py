def get_clear_slug(email: str) -> str:
    indx = email.find("@")
    return email[:indx]


def get_path_for_avatar(instance, filename) -> str:
    """
    :param instance: User
    :param filename: filename
    :return:
    """

    return f"resumes/{instance.employee.user.email}/{instance.id}/{filename}"


def get_path_for_photo_feedback(instance, filename) -> str:
    """
    :param instance: Feedback
    :param filename: filename
    :return:
    """

    return f"feedback/{instance.user.email}/{instance.id}/{filename}"


def get_path_for_image_project(instance, filename) -> str:
    """
    :param instance: Project
    :param filename: filename
    :return:
    """

    return f"projects/{instance.employee.user.email}/{filename}"
