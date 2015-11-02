from django.shortcuts import render
from .models import matriaspirant
from .forms import regform
from django.http import HttpResponse
from django.shortcuts import redirect
from wkhtmltopdf.views import PDFTemplateView
from django.contrib.auth.decorators import login_required

# https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield


# def main(request):
# 	return render(request, 'main.html')

class PDFTemp(PDFTemplateView):
	template_name = "pdftemplate.html"
	title = "just test"




PDFTempview = login_required(PDFTemp.as_view())	


def main(request):

	if request.method == 'POST':
		form = regform(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			# return redirect('main')
			form = regform(initial={'creator': request.user})
			return render(request, 'main.html',{'form':form, 'msg': "Success",'alerttype' : "success"})
		else:
			return render(request, 'main.html',{'form':form, 'msg': "Failed",'alerttype' : "danger"})
	else:
		form = regform(initial={'creator': request.user})
	return render(request, 'main.html',{'form':form})