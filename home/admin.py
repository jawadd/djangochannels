from django.contrib import admin
from .models import ChatGroup,Chat

# Register your models here.
@admin.register(Chat)
class ChatModelAdmin(admin.ModelAdmin):
    list_display=['id','content','timestamp','group']

@admin.register(ChatGroup)
class GroupModelAdmin(admin.ModelAdmin):
    list_display=['id','name']

