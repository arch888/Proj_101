from django.db import models

# Create your models here.


class model_register(models.Model):
	app_name=models.CharField(max_length=50,blank=True)

	def __str__(self):
		return self.app_name
