from django.db import models

# Create your models here.


class Detail(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.fullname
