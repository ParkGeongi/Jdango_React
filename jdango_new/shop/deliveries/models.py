from django.db import models

# Create your models here.
class Delivery(models.Model):
    use_in_migration = True
    delivery_id = models.AutoField(primary_key=True)
    username = models.TextField()
    address = models.TextField()
    detailed_address = models.TextField()
    phone = models.TextField()

    class Meta:
        db_table = 'shop_deliveries'

    def __str__(self):
        return f'{self.pk} {self.username} {self.address} {self.detailed_address} {self.phone}'
