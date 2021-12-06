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
        ordering = ['order', ]

    def __str__(self):
        return self.english_name


class Highlight(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField(null=True, blank=True)
    image_filename = models.CharField(max_length=50, null=True, blank=True)
    link = models.CharField(max_length=1000, null=True, blank=True)
    link_caption = models.CharField(max_length=1000, default='more‥')  # …
    order = models.IntegerField(default=1)
    visible = models.BooleanField(default=True)

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
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['semester', 'order', ]

    def __str__(self):
        return '{} ({})'.format(self.title, self.semester)
