from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=150)
    mobile = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name



class product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to="product")

    def __str__(self) -> str:
        return self.product_name


