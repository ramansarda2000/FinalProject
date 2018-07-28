from django.contrib import admin

# Register your models here.
from .models import Blog
from polls.models import Question, Choice
admin.site.register(Blog)

