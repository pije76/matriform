from django.shortcuts import render
from .models import matriaspirant
from .forms import regform, matriusercreateform
from django.http import HttpResponse
from django.shortcuts import redirect
from wkhtmltopdf.views import PDFTemplateView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class MatriaspirantDetailView(DetailView):

    queryset = matriaspirant.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(MatriaspirantDetailView, self).get_object()
        # Record the last accessed date
        # object.last_accessed = timezone.now()
        # object.save()
        # Return the object
        return object

# https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield


# def main(request):
#   return render(request, 'main.html')

class PDFTemp(PDFTemplateView):
    template_name = "v.html"
    title = "just test"


class PDF(TemplateView):
    template_name = "v.html"
    title = "just test"


class UserCreate(CreateView):
    model = User
    success_url = '/createuser/'
    fields = ['username', 'password', 'is_superuser', 'is_staff']


class matriaspirantUpdate(UpdateView):
    model = matriaspirant
    # fields = ['profilepic','name','gender','caste']
    form_class = matriusercreateform


class OrderListJson(BaseDatatableView):
    # The model we're going to show
    model = matriaspirant
    columns = ['profilepic.url', 'name', 'gender', 'caste', 'dob', 'qualification', 'father_nativeplace_district',
               'address_district', 'id']

    def prepare_results(self, qs):
        # prepare list with output column data
        # queryset is already paginated here
        json_data = []
        for item in qs:
            json_data.append([
                item.profilepic.url if item.profilepic else "",
                item.name,
                item.gender,
                item.caste,
                item.dob.strftime("%d-%m-%Y"),
                item.qualification,
                item.father_nativeplace_district,
                item.address_district,
                item.id
            ])
        return json_data

    def get_initial_queryset(self):
        if not self.request.user.is_superuser:
                # return self.request.user.matriaspirant_set.all()
            return self.request.user.matriaspirant_set.filter(matriaspirant_status="F")
        # return self.model.objects.all()
        return self.model.objects.filter(matriaspirant_status="F")


class M_OrderListJson(BaseDatatableView):
        # The model we're going to show
    model = matriaspirant
    columns = ['profilepic.url', 'name',  'gender','caste', 'dob', 'qualification', 'father_nativeplace_district',
               'address_district', 'id']

    def get_initial_queryset(self):
        if not self.request.user.is_superuser:
            # return self.request.user.matriaspirant_set.all()
            return self.request.user.matriaspirant_set.filter(matriaspirant_status="M")
        # return self.model.objects.all()
        return self.model.objects.filter(matriaspirant_status="M")


class B_OrderListJson(BaseDatatableView):
        # The model we're going to show
    model = matriaspirant
    columns = ['profilepic.url', 'name', 'gender','caste', 'dob', 'qualification', 'father_nativeplace_district',
               'address_district', 'id']

    def get_initial_queryset(self):
        if not self.request.user.is_superuser:
            # return self.request.user.matriaspirant_set.all()
            return self.request.user.matriaspirant_set.filter(matriaspirant_status="B")
        # return self.model.objects.all()
        return self.model.objects.filter(matriaspirant_status="B")

olistjson = login_required(OrderListJson.as_view())
molistjson = login_required(M_OrderListJson.as_view())
bolistjson = login_required(B_OrderListJson.as_view())

PDFTempview = login_required(PDFTemp.as_view())
user_create = login_required(UserCreate.as_view())


def main(request):

    if request.method == 'POST':
        form = regform(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # return redirect('main')
            form = regform(initial={'creator': request.user})
            return render(request, 'main.html', {'form': form, 'msg': "Success", 'alerttype': "success"})
        else:
            return render(request, 'main.html', {'form': form, 'msg': "Failed", 'alerttype': "danger"})
    else:
        form = regform(initial={'creator': request.user})
    return render(request, 'main.html', {'form': form})


@login_required
def move_to_married(request,pk):
    aspirant = get_object_or_404(matriaspirant,pk=pk)
    aspirant.matriaspirant_status = 'M'
    aspirant.save()
    if aspirant.matriaspirant_status is 'M':
        return HttpResponse('success move_to_married')
    else :
        return HttpResponse('fail move_to_married')


@login_required
def move_to_bin(request,pk):
    aspirant = get_object_or_404(matriaspirant,pk=pk)
    aspirant.matriaspirant_status = 'B'
    aspirant.save()
    if aspirant.matriaspirant_status is 'B':
        return HttpResponse('success move_to_bin')
    else :
        return HttpResponse('fail move_to_bin')

@login_required
def restore_to_fresh(request,pk):
    aspirant = get_object_or_404(matriaspirant,pk=pk)
    aspirant.matriaspirant_status = 'F'
    aspirant.save()
    if aspirant.matriaspirant_status is 'F':
        return HttpResponse('success restore_to_fresh')
    else :
        return HttpResponse('fail restore_to_fresh')

