from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Theater_ticket(models.Model):
    use_in_migration = True
    theater_ticket_id = models.AutoField(primary_key=True)#auto increment 되는 IntegerField이다
    x = models.IntegerField()
    y = models.IntegerField()

    class Meta:
        db_table = 'movie_theater_tickets'

    def __str__(self):
        return f'{self.pk} {self.x} {self.y}'

