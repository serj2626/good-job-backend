from django.contrib.auth import user_logged_in, user_logged_out
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()



# Статус пользователя
@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    user.online = True
    user.save()


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    user.online = False
    user.save()


# # Создание профиля пользователя
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
