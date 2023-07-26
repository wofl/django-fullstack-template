from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model.
    https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model
    """
    pass
