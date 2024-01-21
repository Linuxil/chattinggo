from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Users(AbstractUser):
    image = models.ImageField(upload_to='user_image', blank=True,null=True)
    password = models.CharField(max_length=20, null=True)
    last_active = models.CharField(max_length=256, blank=True,null=True)

    def __str__(self) -> str:
        return self.first_name

class Messages(models.Model):
    sender = models.ForeignKey(Users, blank=True, on_delete=models.CASCADE, related_name='my_messages')
    receiver = models.ForeignKey(Users, blank=True, on_delete=models.CASCADE, related_name='other_messages')
    message_date = models.DateTimeField(auto_now_add=True)
    message_body = models.TextField(blank=True)