from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Coach)
admin.site.register(models.Highlight)
admin.site.register(models.Semester)
admin.site.register(models.Course)
