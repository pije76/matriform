from django.forms import ModelForm
from .models import matriaspirants
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class regform(ModelForm):

	class Meta:
		model = matriaspirants
		exclude = []
		widgets = {
            'dob': forms.DateInput(attrs={'class':'datepicker'}, ),
        }

	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.fields['dob'].widget.format = '%d/%m/%Y'
		# at the same time, set the input format on the date field like you want it:
		self.fields['dob'].input_formats = ['%d/%m/%Y']
		self.helper = FormHelper(self)