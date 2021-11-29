from django.db import models

# Create your models here.


class Coach(models.Model):
    english_name = models.CharField(max_length=50, unique=True)
    persian_name = models.CharField(max_length=50, unique=True)
    order = models.IntegerField(default=1)
    category = models.CharField(max_length=50)
    cv = models.TextField()
    email = models.CharField(max_length=50, null=True, blank=True)
    whatsappId = models.CharField(max_length=50, null=True, blank=True)
    instagramId = models.CharField(max_length=50, null=True, blank=True)
    phoneNumber = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.english_name
