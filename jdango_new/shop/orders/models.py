from django.db import models

from security.seq_users.models import SeqUser
from shop.deliveries.models import Delivery
from shop.products.models import Product



# Create your models here.
class Order(models.Model):
    use_in_migration = True
    order_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(SeqUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    deliveries = models.ForeignKey(Delivery, on_delete=models.CASCADE)

    class Meta:
        db_table = 'shop_orders'

    def __str__(self):
        return f'{self.pk} {self.created_at}'
