from django.db import models
# Create your models here.

class User(models.Model):
    use_in_migrations = True
    user_id = models.IntegerField(primary_key=True,max_length=30)
    username = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField()
    rank= models.IntegerField()
    point = models.TextField()
    class Meta:
            db_table = 'users'

    def __str__(self):
        return f'{self.user_id} {self.username} {self.password} {self.created_at} {self.rank} {self.point}'