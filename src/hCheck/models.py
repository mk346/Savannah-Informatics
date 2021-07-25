from django.db import models

# Create your models here.
# creating a database table to store the given data
class healthSys(models.Model):
	hName = models.CharField(max_length=200, blank=False)
	county = models.CharField(max_length=100, blank=False)
	system = models.CharField(max_length=200, blank=True)
	sVersion = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.hName
