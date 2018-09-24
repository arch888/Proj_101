from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,get_user_model



def index(request):
	return render(request,"index/index.html",{})