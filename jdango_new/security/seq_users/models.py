from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser


class SeqUser(models.Model):
    # These fields tie to the roles!
    ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee')
    )

    use_in_migrations = True
    susers_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    birth = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    user_interests = models.CharField(max_length=20)
    token = models.CharField(max_length=20)
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        db_table = "seq_users"
        verbose_name = 'seq_user'
        verbose_name_plural = 'seq_users'