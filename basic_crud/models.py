from django.db import models
from  django.utils import timezone

# Create your models here.


class Detail(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)
    profile = models.ImageField(default='IMAGE',upload_to='profile/')
    date_added = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.fullname
