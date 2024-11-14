def get_path_for_photo_feedback(instance, filename) -> str:
    return f"feedback/{instance.user.email}/{instance.id}/{filename}"
