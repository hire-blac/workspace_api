from django.db import models
from workspace.unique import unique_slug_generator

# Create your models here.
class Space(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name

    # overwrite save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, self.name)
        return super().save(*args, **kwargs)

class Plan(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name

    # overwrite save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, self.name)
        return super().save(*args, **kwargs)

class Booking(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE, related_name='space')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='plan')
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return f'{self.plan} plan for {self.space}'

    # overwrite save method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, self.plan)
        return super().save(*args, **kwargs)

class BookedDay(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='booking')
    day = models.IntegerField()
    date_of_day = models.DateField(auto_now=False, auto_now_add=False)
    hours = models.IntegerField()
    starting_time = models.IntegerField(default=9)
    ending_time = models.IntegerField(default=17)
    # starting_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    # ending_time = models.DateTimeField(auto_now=False, auto_now_add=False)

