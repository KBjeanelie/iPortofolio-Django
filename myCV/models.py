from django.db import models

# Create your models here.
from django.utils.text import slugify


class Skills(models.Model):
    label = models.CharField(max_length=50, verbose_name="label")
    pourcentage = models.IntegerField(verbose_name="Pourcentage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Competence en " + str(self.label)


class Category(models.Model):
    label = models.CharField(max_length=20, verbose_name="label")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.label)


class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Portfolio",
                                 verbose_name="Project's category")
    client = models.CharField(max_length=50, verbose_name="Client ")
    slug = models.SlugField()
    project_date = models.CharField(max_length=50, verbose_name="Portfolio Date")
    project_url = models.URLField(verbose_name="Portfolio URL")
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    img_one = models.ImageField(upload_to="image/", verbose_name="Image 1")
    img_two = models.ImageField(upload_to="image/", verbose_name="Image 2")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        s = str(self.title) + ":" + str(self.client)
        self.slug = slugify(s, allow_unicode=True)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return "projet " + str(self.title)


class Education(models.Model):
    degrees = models.CharField(max_length=50, verbose_name="Degrees ")
    period = models.CharField(max_length=20, verbose_name="Period ")
    description = models.TextField(verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.degrees)


class Testimonials(models.Model):
    full_name = models.CharField(max_length=50, verbose_name="Fullname ")
    job = models.CharField(max_length=50, verbose_name="Professional status")
    opinion = models.TextField(verbose_name="Your Opinons")
    validated = models.BooleanField(default=False, verbose_name="validate")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
