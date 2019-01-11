from django.contrib import admin

# Register your models here.
from .models import Question, Sub_Topic

admin.site.register(Question)
admin.site.register(Sub_Topic)