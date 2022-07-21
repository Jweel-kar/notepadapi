# Create your models here.
from django.db import models


# Create your models here.
class Notepad(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  title = models.TextField(
    max_length=200,
    null=False,
    blank=False
  )

  text = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  creation_date = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False
  )

  last_updated = models.DateTimeField(
    auto_now=True,
    null=False,
    blank=False
  )

  class Meta:
    db_table = 'Notepads'
