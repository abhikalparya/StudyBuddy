from django.contrib import admin
from .models import Room, Message, Topic, User

# Register your models here.

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)