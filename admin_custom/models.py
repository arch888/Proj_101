from django.db import models
import random
import os

# Create your models here.

def get_filename_ext(filepath):
	base_name=os.path.basename(filepath)
	name ,ext=os.path.splitext(base_name)
	return name ,ext

def upload_image_path(instance,filename):
	new_filename=random.randint(1,13516546431654)
	name ,ext=get_filename_ext(filename)
	final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	return "product/{final_filename}".format(
		new_filename=new_filename,
		final_filename=final_filename
		)





class model_register(models.Model):
	app_name=models.CharField(max_length=50,blank=True)
	app_path=models.CharField(max_length=255,blank=False)
	image=models.ImageField(upload_to=upload_image_path,null=True,blank=True)

	def __str__(self):
		return self.app_name
