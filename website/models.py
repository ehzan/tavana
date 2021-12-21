from django.db import models
from django_jalali.db import models as jmodels
import jdatetime

# Create your models here.


class Coach(models.Model):
    english_name = models.CharField(max_length=50, unique=True)
    persian_name = models.CharField(max_length=50, unique=True)
    order = models.IntegerField(default=10)
    category = models.CharField(max_length=50)
    cv = models.TextField()
    email = models.CharField(max_length=50, null=True, blank=True)
    whatsappId = models.CharField(max_length=50, null=True, blank=True)
    instagramId = models.CharField(max_length=50, null=True, blank=True)
    phoneNumber = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.english_name


class Highlight(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=1000, null=True, blank=True)
    image_filename = models.CharField(max_length=50, null=True, blank=True)
    link = models.CharField(max_length=1000, null=True, blank=True)
    link_caption = models.CharField(max_length=1000, default='more‥')  # …
    header = models.BooleanField(default=False)
    body = models.BooleanField(default=False)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.title


class Semester(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    active = models.BooleanField(default=False)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    description = models.TextField(null=True, blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    order = models.IntegerField(default=10)

    class Meta:
        ordering = ['semester', 'order', ]

    def __str__(self):
        return '{} ({})'.format(self.title, self.semester)


class Page(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image_filename_1 = models.CharField(max_length=50, null=True, blank=True)
    image_caption_1 = models.CharField(max_length=1000, null=True, blank=True)
    image_filename_2 = models.CharField(max_length=50, null=True, blank=True)
    image_caption_2 = models.CharField(max_length=1000, null=True, blank=True)
    image_filename_3 = models.CharField(max_length=50, null=True, blank=True)
    image_caption_3 = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=10)
    date = jmodels.jDateField(null=True, default=jdatetime.date.today())
    image_filename_1 = models.CharField(max_length=50, null=True, blank=True)
    image_caption_1 = models.CharField(max_length=1000, null=True, blank=True)
    image_filename_2 = models.CharField(max_length=50, null=True, blank=True)
    image_caption_2 = models.CharField(max_length=1000, null=True, blank=True)
    image_filename_3 = models.CharField(max_length=50, null=True, blank=True)
    image_caption_3 = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = "News"
        ordering = ['order', 'date', ]

    def __str__(self):
        return self.title


class video(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=1000, null=True, blank=True)
    order = models.IntegerField(default=10)
    date = jmodels.jDateField(null=True, default=jdatetime.date.today())

    class Meta:
        ordering = ['order', 'date', ]

    def __str__(self):
        return self.title
