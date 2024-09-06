from django.apps import AppConfig
# from django.db.utils import IntegrityError
# from django.contrib.auth import get_user_model


class LiveroomConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "liveroom"

    # def ready(self):
    #     User = get_user_model()
    #     username = 'admin'
    #     email = 'admin@example.com'
    #     password = 'admin'

    #     if not User.objects.filter(username=username).exists():
    #         try:
    #             User.objects.create_superuser(username, email, password)
    #             print('Successfully created new superuser')
    #         except IntegrityError:
    #             print('Could not create superuser')