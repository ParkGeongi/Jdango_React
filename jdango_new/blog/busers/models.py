from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Buser(models.Model):
    use_in_migration = True
    blog_userid = models.AutoField(primary_key=True)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()


    class Meta:
        db_table = 'blog_busers'
    def __str__(self):
        return f'{self.pk} {self.email} {self.nickname} {self.password}'
