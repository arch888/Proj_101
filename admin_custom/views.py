from django.shortcuts import render
from .forms import create_model
import shutil
import os
from .models import model_register as m_r

# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def admin_custom(request):
	return render(request,"admin/admin_home.html",{})


def admin_create_model(request):
	form_class=create_model(request.POST or None)
	context={
		"form":form_class,
	}
	if form_class.is_valid():
		app_name=form_class.cleaned_data.get('model_name')
		#object=m_r.objects.create(app_name=app_name)
		#os.makedirs(os.path.join(BASE_DIR, app_name))
		shutil.copytree(os.path.join(BASE_DIR, 'sampleapp'),os.path.join(BASE_DIR, app_name))
		exact_file=os.path.join(BASE_DIR, app_name)+"/apps.py"
		file=open(exact_file,"w")
		content="""from django.apps import AppConfig


class SampleappConfig(AppConfig):
    name = '"""+app_name+"""'"""
		file.write(content)
		file.close()
	return render(request,"admin/admin_create_form.html",context)