from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="foods/%Y/%m/%d/")
    price = models.FloatField(max_length=10)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    fullname = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return str(self.food)
