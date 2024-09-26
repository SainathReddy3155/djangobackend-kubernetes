from django.db import models
from random import randint

# Create your models here.
def generate_radnom_num():
    return randint(10000,99999)

class AddProduct(models.Model):
    product_id=models.IntegerField(default=generate_radnom_num,null=False,unique=True,editable=False)
    product_name=models.CharField(max_length=100,null=False)
    cost=models.FloatField(max_length=10,null=False)
    rating=models.FloatField(max_length=5,null=False)
    status=models.CharField(max_length=15,null=False)


    def __str__(self):
        return self.product_name