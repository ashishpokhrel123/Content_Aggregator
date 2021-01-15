from django.contrib import admin
from .models import Category, Subscrition, Article

# Register your models here.
admin.site.register(Category)
admin.site.register(Subscrition)
admin.site.register(Article)