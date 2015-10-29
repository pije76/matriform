from django.forms import ModelForm
from .models import matriaspirant
from django import forms
from crispy_forms.helper import FormHelper


class regform(ModelForm):
	

	class Meta:
		model = matriaspirant
		exclude = []
		widgets = {
            'dob': forms.DateInput(attrs={'class':'datepicker'}, ),
          	'creator':forms.HiddenInput()}

	def __init__(self, *args, **kwargs):
		super(regform, self).__init__(*args, **kwargs)
		self.fields['dob'].widget.format = '%d/%m/%Y'
		# at the same time, set the input format on the date field like you want it:
		self.fields['dob'].input_formats = ['%d/%m/%Y']
		# self.helper = FormHelper(self)
		# self.helper.layout.append(Submit('save', 'save'))
		