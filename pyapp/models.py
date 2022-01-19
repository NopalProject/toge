from django.db import models
import datetime

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	fechaCreacion = models.DateTimeField(auto_now_add=True, blank=True)
	
	def __str__(self):
		return f"{self.username} creado el {self.fechaCreacion.strftime('%d, %b, %Y')}"
