def get_clear_slug(email: str) -> str:
    indx = email.find("@")
    return email[:indx]


def get_path_for_avatar(instance, filename) -> str:
    return f"resumes/{instance.employee.user.email}/{instance.id}/{filename}"


def get_path_for_photo_feedback(instance, filename) -> str:
    return f"feedback/{instance.user.email}/{instance.id}/{filename}"
