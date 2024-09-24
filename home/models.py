from django.db import models

# Create your models here.

class ChatGroup(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
class Chat(models.Model):
    content= models.CharField(max_length=1000)
    timestamp= models.DateField(auto_now=True)
    group= models.ForeignKey(ChatGroup, on_delete=models.CASCADE)

