from django.forms import ModelForm
from .models import matriaspirant
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset,ButtonHolder, Submit , HTML,Row, Div
import crispy_forms.layout
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class MyAuthenticationForm(AuthenticationForm):
	pass
	

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
		self.fields['tob'].label = "वेऴ(Time)"
		self.fields['dob'].label = "जन्म तारीख(DOB)"
		self.fields['name'].label = "मुलाचे नाव / मुलीचे नाव(Name of Candidate)"
		self.fields['height'].label = "उंची(Height)"
		self.fields['caste'].label = "जात्(caste)"
		self.fields['complexion'].label = "रंग / वर्ण(Complexion)"
		self.fields['birth_place'].label = "जन्म ठिकाण(Birth Place)"
		self.fields['qualification'].label = "शिषन(Qualification)"
		self.fields['course_hobbie'].label = "कोर्स / छंद(Course / Hobbies)"
		self.fields['occupation'].label = "नोकरी(Occupation)"
		self.fields['business'].label = "य़वसाय(Business)"
		self.fields['agriculture'].label = "शेती(Agriculture)"
		self.fields['house'].label = "घर(House)"
		self.fields['income'].label = "उतप्न(Income)"
		self.fields['father_occupation'].label = "वडिलांची नोकरी/य़वसाय(Father's Occupation)"
		self.fields['mother_occupation'].label = "आईची नोकरी/य़वसाय(Mother's Occupation) "
		self.fields['father_name'].label = "वडिलांचे पुर्ण नाव(Father's Full Name)"

		self.fields['father_nativeplace'].label = "वडिलांचे मुऴ गाव(Father's Native Place)"
		self.fields['mother_nativeplace'].label = "आईची मुऴ गाव(Mother's Native Place)"
		self.fields['num_brothers'].label = "भाऊ(Brothers)"
		self.fields['num_brothers_married'].label = "विवाहित(Married)"
		self.fields['num_brothers_unmarried'].label = "अविवाहित(Unmarried)"
		self.fields['num_sisters'].label = "जन्म तारीख(DOB)"
		self.fields['num_sisters_married'].label = "जन्म तारीख(DOB)"
		self.fields['num_sisters_unmarried'].label = "जन्म तारीख(DOB)"
		self.fields['expectations'].label = "मुला / मुली बदल्ल अपेशा(Expectation's)"
		self.fields['mobile'].label = " मोबाईल(Mobile)"
		self.fields['phone'].label = "फोन(Phone)"
		self.fields['address'].label = "सध्याचा पता(Current Postal Adress)"
		# self.helper.layout.append(Submit('save', 'save'))
		self.helper = FormHelper(self)
		# self.helper.form_class = 'form-horizontal'

		# self.helper.label_class = 'col-md-3'
		# self.helper.field_class = 'col-md-3'
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			'creator','profilepic',
			Fieldset('Candidate\'s Personal Info',Div('name', 'gender', css_class='row'), 
				Div('dob', 'tob', css_class='row'),Div('height', 'caste', css_class='row'),
				Div('complexion', 'birth_place', css_class='row'),Div('qualification',
				 'course_hobbie', css_class='row'),Div('occupation', 'business',
				  css_class='row'),Div('agriculture', 'house', css_class='row'),
				 Div('income', css_class='row'),),
			Fieldset('Family Info',Div('father_occupation', 'mother_occupation', css_class='row'),
			Div('father_name', 'father_nativeplace', css_class='row') ,
			Div('mother_nativeplace', 'num_brothers', css_class='row'),
			Div('num_brothers_married', 'num_brothers_unmarried', css_class='row'),
			Div('num_sisters', 'num_sisters_married', css_class='row'),
			Div('num_sisters_unmarried', css_class='row'),),
			Fieldset('Expectations',Div('expectations', css_class='row')),
			Fieldset('सपंर्क(Contact)',Div('mobile', 'phone', css_class='row'),
			Div('address', css_class='row')),
      HTML('<div class="container">'), 
      Submit('submit', 'Register',css_class='ghost-button'), 
      HTML('</div>'),
    )
		# self.helper[2][0].wrap_together(crispy_forms.layout.Div, css_class="row")
		self.helper['name'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['gender'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2 ")
		self.helper['dob'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1 clearfix")
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

		self.helper['expectations'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-10 col-md-offset-1")

		self.helper['mobile'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4  col-md-offset-1")
		self.helper['phone'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2")
		self.helper['address'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-10 col-md-offset-1")
		
	