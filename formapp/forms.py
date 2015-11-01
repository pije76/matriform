from django.forms import ModelForm
from .models import matriaspirant
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit , HTML
import crispy_forms.layout


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
		self.fields['tob'].label = "Time of birth"
		self.fields['dob'].label = "Date of birth"
		self.fields['name'].label = "मुलाचे नाव / मुलीचे नाव(Name of Candidate)"
		# self.helper = FormHelper(self)
		# self.helper.layout.append(Submit('save', 'save'))
		self.helper = FormHelper(self)
		# self.helper.form_class = 'form-horizontal'

		# self.helper.label_class = 'col-md-3'
		# self.helper.field_class = 'col-md-3'
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			'profilepic',
			Fieldset('Candidate\'s Personal Info','name', 'gender', 'dob', 'tob','height','caste',
				'complexion','birth_place','qualification','course_hobbie','occupation','business',
				'agriculture','house','income'),
			Fieldset('Family Info','father_occupation', 'mother_occupation', 'father_name', 'father_nativeplace',
			 'mother_nativeplace','num_brothers','num_brothers_married','num_brothers_unmarried',
			 'num_sisters','num_sisters_married','num_sisters_unmarried'),
			Fieldset('Expectations','expectations'),
			Fieldset('Contact Info','mobile','phone', 'address'),
      HTML('<div class="container">'), 
      Submit('submit', 'Register',css_class='ghost-button'), 
      HTML('</div>'),
    )
		self.helper[0:2].wrap_together(crispy_forms.layout.Div, css_class="row")
		self.helper['name'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['gender'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2")
		self.helper['dob'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['tob'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2")
		self.helper['height'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['caste'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4  col-md-offset-2")
		self.helper['complexion'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['birth_place'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2")
		self.helper['qualification'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['course_hobbie'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4  col-md-offset-2")
		self.helper['occupation'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['business'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4  col-md-offset-2")
		self.helper['agriculture'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['house'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4  col-md-offset-2")
		self.helper['income'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")

		self.helper['father_occupation'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['mother_occupation'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2")
		self.helper['father_name'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['father_nativeplace'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2")
		self.helper['mother_nativeplace'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['num_brothers'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4  col-md-offset-2")
		self.helper['num_brothers_married'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['num_brothers_unmarried'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2")
		self.helper['num_sisters'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4  col-md-offset-1")
		self.helper['num_sisters_married'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2")
		self.helper['num_sisters_unmarried'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")

		self.helper['expectations'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-8 col-md-offset-2")

		self.helper['mobile'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4  col-md-offset-1")
		self.helper['phone'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2")
		self.helper['address'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-8 col-md-offset-2")
		