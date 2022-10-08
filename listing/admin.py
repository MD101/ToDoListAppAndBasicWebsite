from django.contrib import admin
from . import models
# Register your models here.

class ToDoListAdmin(admin.ModelAdmin):
    List_display = ( 'title' , 'created_time_stamp' , 'description' , 'due_date' , 'category')

class CategoryAdmin(admin.ModelAdmin):
    List_display = ( 'name', )

admin.site.register(models.Category_of_List, ToDoListAdmin)
admin.site.register(models.Listing, CategoryAdmin)
