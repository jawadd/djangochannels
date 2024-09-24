from django.shortcuts import render

# Create your views here.

def index(request,group_name):

    return render(request,'home/index.html',{'groupName':group_name})