from django import forms


from .models import model_register as m_r


class create_model(forms.Form):
	model_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the Model Name"}))
	def clean_model_name(self):
		name=self.cleaned_data.get("model_name")
		qs=m_r.objects.filter(app_name=name)
		if qs.exists():
			raise forms.ValidationError("App Name is Taken please take any other name !")
		return name






	# username=forms.CharField(widget=forms.TextInput(attrs={"class":"email","placeholder":"Your Username or Roll No"}))
	# name=forms.CharField( widget=forms.TextInput(attrs={"class":"email","placeholder":"Your Name"}))
	# email=forms.CharField( widget=forms.TextInput(attrs={"class":"email","placeholder":"Your Email"}))
	# password=forms.CharField( widget=forms.PasswordInput(attrs={ "placeholder":"Password"}))
	# password1=forms.CharField( label="Confirm Password",widget=forms.PasswordInput(attrs={ "placeholder":"Confirm Password"}))
	# CHOICES=[('select1','Staff'),('select2','Customer')]
	# like= forms.ChoiceField(choices=CHOICES, label="Type of User",widget=forms.RadioSelect())

	# def clean_username(self):
	# 	username=self.cleaned_data.get("username")
	# 	qs=User.objects.filter(username=username)
	# 	if qs.exists():
	# 		raise forms.ValidationError("Username Taken !")
	# 	return username
	# def clean(self):
	# 	data=self.cleaned_data
	# 	password=self.cleaned_data.get("password")
	# 	password1=self.cleaned_data.get("password1")
	# 	if password1 != password:
	# 		raise forms.ValidationError("Password must Match !")
	# 	return data