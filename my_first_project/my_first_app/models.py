from django.db import models

# Create your models here.


class Car(models.Model):
    title = models.TextField(max_length=250)
    years = models.TextField(max_length=4, null=True)

    def __str__(self):
        return f"Car Info: Model-> {self.title}, Year-> {self.years}"

