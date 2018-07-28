from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
	"""This is basic class of the blog"""
	title = models.CharField(max_length=200)
	created = models.DateTimeField(timezone.now())
	body = models.TextField('Body Text', default='Some text')
	id = models.IntegerField(primary_key=True)

	def __str__(self):
		return self.title
