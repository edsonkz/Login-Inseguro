from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Mensagem(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    mensagem = models.TextField(null=False)
