from django.forms import ModelForm
from .models import matriaspirant
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset,ButtonHolder, Submit , HTML,Row, Div
import crispy_forms.layout
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput



class matriusercreateform(ModelForm):
	class Meta:
		model = matriaspirant
		exclude = []
		widgets = {
            'dob': forms.DateInput(attrs={'class':'datepicker'}, ),
          	'creator':forms.HiddenInput()}

	def __init__(self, *args, **kwargs):
		super(matriusercreateform, self).__init__(*args, **kwargs)
		self.fields['dob'].widget.format = '%d/%m/%Y'
		# at the same time, set the input format on the date field like you want it:
		self.fields['dob'].input_formats = ['%d/%m/%Y']
		self.fields['tob'].label = "वेळ(Time)"
		self.fields['dob'].label = "जन्म तारीख(DOB)"
		self.fields['name'].label = "मुलाचे नाव / मुलीचे नाव(Name of Candidate)"
		self.fields['height'].label = "उंची(Height)"
		self.fields['caste'].label = "जात्(caste)"
		self.fields['complexion'].label = "रंग / वर्ण(Complexion)"
		self.fields['birth_place'].label = "जन्म ठिकाण(Birth Place)"
		self.fields['qualification'].label = "सिक्षण(Qualification)"
		self.fields['course_hobbie'].label = "कोर्स / छंद(Course / Hobbies)"
		self.fields['occupation'].label = "नोकरी(Occupation)"
		self.fields['business'].label = "व्यवसाय(Business)"
		self.fields['agriculture'].label = "शेती(Agriculture)"
		self.fields['house'].label = "घर(House)"
		self.fields['income'].label = "उत्पन्न(Income)"
		self.fields['blood_group'].label = "रक्त्तगट(Blood Group)"
		self.fields['father_occupation'].label = "वडिलांचे नोकरी/व्यवसाय(Father's Occupation)"
		self.fields['mother_occupation'].label = "आईचे नोकरी/व्यवसाय(Mother's Occupation) "
		self.fields['father_name'].label = "वडिलांचे पुर्ण नाव(Father's Full Name)"

		self.fields['father_nativeplace'].label = "वडिलांचे मुळ गाव(Father's Native Place)"
		self.fields['father_nativeplace_district'].label = "जिल्हा(District)"
		self.fields['mother_nativeplace'].label = "आईचे मुळ गाव(Mother's Native Place)"
		self.fields['num_brothers'].label = "भाऊ(Brothers)"
		self.fields['num_brothers_married'].label = "विवाहित(Married)"
		self.fields['num_brothers_unmarried'].label = "अविवाहित(Unmarried)"
		self.fields['num_sisters'].label = "बहीण(Sister)"
		self.fields['num_sisters_married'].label = "विवाहित बहीण(Married)"
		self.fields['num_sisters_unmarried'].label = "अविवाहित बहीण(Unmarried)"
		self.fields['expectations'].label = "मुला / मुली बदल्ल अपेक्षा(Expectation's)"
		self.fields['mobile'].label = " भ्रमणध्वनी(Mobile)"
		self.fields['phone'].label = "दूरध्वनी(Phone)"
		self.fields['address'].label = "सध्याचा पत्रव्यवहाराचा पत्ता(Current Postal Adress)"
		self.fields['address_district'].label = "जिल्हा(District)"
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
				 Div('income','blood_group', css_class='row'),),
			Fieldset('कौटुंबिक माहिती(Family Info)',Div('father_occupation', 'mother_occupation', css_class='row'),
			Div('father_name', 'father_nativeplace','father_nativeplace_district', css_class='row') ,
			Div('mother_nativeplace', 'num_brothers', css_class='row'),
			Div('num_brothers_married', 'num_brothers_unmarried', css_class='row'),
			Div('num_sisters', 'num_sisters_married', css_class='row'),
			Div('num_sisters_unmarried', css_class='row'),),
			Fieldset('(अपेक्षा)Expectations',Div('expectations', css_class='row')),
			Fieldset('सपंर्क(Contact)',Div('address','address_district', css_class='row')),
			Div('mobile', 'phone', css_class='row'),
      HTML('<div class="container">'), 
      Submit('submit', 'Update',css_class='ghost-button'), 
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
		self.helper['blood_group'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2")

		self.helper['father_occupation'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['mother_occupation'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2")
		self.helper['father_name'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-3 col-md-offset-1")
		self.helper['father_nativeplace'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 ")
		self.helper['father_nativeplace_district'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-3 ")
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
		self.helper['address'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-8 col-md-offset-1")
		self.helper['address_district'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-2 ")


class MyAuthenticationForm(AuthenticationForm):
	pass
	

class regform(ModelForm):
	class Meta:
		model = matriaspirant
		exclude = []
		widgets = {
            'dob': forms.DateInput(attrs={'class':'datepicker'}, ),
          	'creator':forms.HiddenInput(),
          	'matriaspirant_status':forms.HiddenInput()
          	}

	def __init__(self, *args, **kwargs):
		super(regform, self).__init__(*args, **kwargs)
		self.fields['dob'].widget.format = '%d/%m/%Y'
		# at the same time, set the input format on the date field like you want it:
		self.fields['dob'].input_formats = ['%d/%m/%Y']
		self.fields['tob'].label = "वेळ(Time)"
		self.fields['dob'].label = "जन्म तारीख(DOB)"
		self.fields['name'].label = "मुलाचे नाव / मुलीचे नाव(Name of Candidate)"
		self.fields['height'].label = "उंची(Height)"
		self.fields['caste'].label = "जात्(caste)"
		self.fields['complexion'].label = "रंग / वर्ण(Complexion)"
		self.fields['birth_place'].label = "जन्म ठिकाण(Birth Place)"
		self.fields['qualification'].label = "सिक्षण(Qualification)"
		self.fields['course_hobbie'].label = "कोर्स / छंद(Course / Hobbies)"
		self.fields['occupation'].label = "नोकरी(Occupation)"
		self.fields['business'].label = "व्यवसाय(Business)"
		self.fields['agriculture'].label = "शेती(Agriculture)"
		self.fields['house'].label = "घर(House)"
		self.fields['income'].label = "उत्पन्न(Income)"
		self.fields['blood_group'].label = "रक्त्तगट(Blood Group)"
		self.fields['father_occupation'].label = "वडिलांचे नोकरी/व्यवसाय(Father's Occupation)"
		self.fields['mother_occupation'].label = "आईचे नोकरी/व्यवसाय(Mother's Occupation) "
		self.fields['father_name'].label = "वडिलांचे पुर्ण नाव(Father's Full Name)"

		self.fields['father_nativeplace'].label = "वडिलांचे मुळ गाव(Father's Native Place)"
		self.fields['father_nativeplace_district'].label = "जिल्हा(District)"
		self.fields['mother_nativeplace'].label = "आईचे मुळ गाव(Mother's Native Place)"
		self.fields['num_brothers'].label = "भाऊ(Brothers)"
		self.fields['num_brothers_married'].label = "विवाहित(Married)"
		self.fields['num_brothers_unmarried'].label = "अविवाहित(Unmarried)"
		self.fields['num_sisters'].label = "बहीण(Sister)"
		self.fields['num_sisters_married'].label = "विवाहित बहीण(Married)"
		self.fields['num_sisters_unmarried'].label = "अविवाहित बहीण(Unmarried)"
		self.fields['expectations'].label = "मुला / मुली बदल्ल अपेक्षा(Expectation's)"
		self.fields['mobile'].label = " भ्रमणध्वनी(Mobile)"
		self.fields['phone'].label = "दूरध्वनी(Phone)"
		self.fields['address'].label = "सध्याचा पत्रव्यवहाराचा पत्ता(Current Postal Adress)"
		self.fields['address_district'].label = "जिल्हा(District)"
		# self.helper.layout.append(Submit('save', 'save'))
		self.helper = FormHelper(self)
		# self.helper.form_class = 'form-horizontal'

		# self.helper.label_class = 'col-md-3'
		# self.helper.field_class = 'col-md-3'
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			'creator','profilepic',
			Fieldset('Candidate\'s Personal Info',Div('name', 'gender', css_class='row'), 
				Div('dob', 'tob','matriaspirant_status', css_class='row'),Div('height', 'caste', css_class='row'),
				Div('complexion', 'birth_place', css_class='row'),Div('qualification',
				 'course_hobbie', css_class='row'),Div('occupation', 'business',
				  css_class='row'),Div('agriculture', 'house', css_class='row'),
				 Div('income','blood_group', css_class='row'),),
			Fieldset('कौटुंबिक माहिती(Family Info)',Div('father_occupation', 'mother_occupation', css_class='row'),
			Div('father_name', 'father_nativeplace','father_nativeplace_district', css_class='row') ,
			Div('mother_nativeplace', 'num_brothers', css_class='row'),
			Div('num_brothers_married', 'num_brothers_unmarried', css_class='row'),
			Div('num_sisters', 'num_sisters_married', css_class='row'),
			Div('num_sisters_unmarried', css_class='row'),),
			Fieldset('(अपेक्षा)Expectations',Div('expectations', css_class='row')),
			Fieldset('सपंर्क(Contact)',Div('address','address_district', css_class='row')),
				Div('mobile', 'phone', css_class='row'),
			
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
		self.helper['blood_group'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2")

		self.helper['father_occupation'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-1")
		self.helper['mother_occupation'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 col-md-offset-2")
		self.helper['father_name'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-3 col-md-offset-1")
		self.helper['father_nativeplace'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-4 ")
		self.helper['father_nativeplace_district'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-3")
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
		self.helper['address'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-8 col-md-offset-1")
		self.helper['address_district'].wrap(crispy_forms.layout.Field, wrapper_class="col-md-2 ")

		
	