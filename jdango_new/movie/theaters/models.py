from django.db import models


# Create your models here.
class Theater(models.Model):
    use_in_migration = True
    theater_id = models.AutoField(primary_key=True)#auto increment 되는 IntegerField이다
    title = models.TextField()
    seat = models.TextField()

    class Meta:
        db_table = 'movie_theaters'

    def __str__(self):
        return f'{self.pk} {self.title} {self.seat}'
