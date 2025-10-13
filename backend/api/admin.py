from django.contrib import admin
from .models import Sign, Video
from django.contrib.auth import get_user_model 

User = get_user_model()
# Register your models here.

admin.site.register(Sign)
admin.site.register(Video)
admin.site.register(User)