from django.contrib import admin
from .models import Blog, Category, Comment, Profile

# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Profile)
#admin.site.register(DevTeam)