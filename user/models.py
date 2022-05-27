from django.db import models

# Create your models here.
class CustomUser(models.Model):
    class Meta:
        db_table = "my_user"

    email = models.EmailField(max_length=128, verbose_name='user_email')
    password = models.CharField(max_length=64, verbose_name='paasword')

