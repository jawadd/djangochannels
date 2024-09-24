from django.shortcuts import render
from .models import ChatGroup,Chat

# Create your views here.

def index(request,group_name):
# Check if the group exists, if not, create it
    group, created = ChatGroup.objects.get_or_create(name=group_name)
    if not created:
        chats = list(Chat.objects.filter(group=group))
    else:
        chats = []

    return render(request, 'home/index.html', {'groupName': group_name,'chats':chats})