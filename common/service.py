def get_clear_slug(email: str) -> str:
    indx = email.find("@")
    return email[:indx]


def get_path_for_avatar(instance, filename) -> str:
    return f"avatars/{instance.user.type}/{instance.user.email}/{filename}"
