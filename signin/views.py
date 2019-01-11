from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemberForm
from .models import Members
from django import forms

def home_view(request):
	template_name = "signin/home.html"
	if request.method == "POST":
		form = MemberForm(request.POST)

		if form.is_valid():
			print("VALID")
			#Validating username and password
			usnt = form.cleaned_data['usn']
			passt = form.cleaned_data['pwd']
			print(usnt, passt)
			#check if username is valid
			objtry = get_object_or_404(Members, usn=usnt)
			if objtry:
				print("Obj is ", objtry)
				#check if password matches
				if objtry.pwd!=passt:
					print("Failure")
					form = MemberForm()
				else:
					#Redirecting to details page
					return render(request, "details/details.html")
		context = {
			'tried': True
		}


	else:
		form = MemberForm()
		context = {
			'tried': False
		}

	return render(request, template_name, {'form': form}, context)
