from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
import datetime

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	fechaCreacion = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return f"{self.username} creado el {self.fechaCreacion.strftime('%d, %b, %Y')}"

class Note(models.Model):
  noteTitle = models.CharField(max_length=50)
  noteBody = models.TextField()
  noteCreatedDate = models.DateTimeField(editable=False)
  noteUpdatedDate = models.DateTimeField()
  enabled = models.BooleanField()
  userId = models.ForeignKey(User, on_delete=models.CASCADE)

  '''Overload of save method'''
  def save(self, *args, **kwargs):
    #On dave Update timestamps
    if not self.id:
      self.noteCreatedDate=timezone.now()
    self.noteUpdatedDate=timezone.now()
    return super(Note, self).save(*args, **kwargs)

  def __str__(self):
    return f"{self.noteTitle}\n{self.noteBody}\n{self.noteCreatedDate}"
