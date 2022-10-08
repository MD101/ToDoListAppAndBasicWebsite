from django.db import models
from django.utils import timezone

# Create your models here.
class Category_of_List(models.Model):
    name = models.CharField(max_length=15)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=200)
    #created_time_stamp = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))
    created_time_stamp = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    #due_date = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateTimeField(default=timezone.now())
    category = models.ForeignKey(Category_of_List,on_delete=models.CASCADE)

    class Meta:
        ordering = ["due_date"]
    def __str__(self):
        return self.title
