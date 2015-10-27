from django.shortcuts import render
from .models import matriaspirants
from .forms import regform
from django.http import HttpResponse
from django.shortcuts import redirect

# https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield

def matrihome(request):
	return	HttpResponse("welcome!")

def registration(request):
	if request.method == 'POST':
		form = regform(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			return render(request, 'reg.html',{'form':form})
	else:
		form = regform()
	return render(request, 'reg.html',{'form':form})