from django.shortcuts import render
from .forms import create_model

# Create your views here.




def admin_custom(request):
	return render(request,"admin/admin_home.html",{})


def admin_create_model(request):
	form_class=create_model(request.POST or None)
	context={
		"form":form_class,
	}
	return render(request,"admin/admin_create_form.html",context)
