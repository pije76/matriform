from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.urlresolvers import reverse





GENDER_CHOICES=(('M','Male'),('F','Female'))
COMPLEXION_CHOICES=(('L','Light'),('F','Fair'),('W','Wheatish'),('D','Dark'))
PROFILE_Status=(('F','Fresh'),('M','Married'),('B','Bin'))
BLOOD_GROUP_CHOICES = (('O+','O +'),('O-','O -'),('A+','A +'),('A-','A -'),
	('B+','B +'),('B-','B -'),('AB+','AB +'),('AB-','AB -'))



class matriaspirant(models.Model):
	#personal info
	profilepic = models.ImageField("Profile Pic", upload_to="images/%Y/%m/%d",null=True, blank=True)
	name = models.CharField(max_length=50)
	gender = models.CharField(max_length=1,default='M',choices=GENDER_CHOICES)
	matriaspirant_status = models.CharField(max_length=1,default='F',choices=PROFILE_Status)
	dob = models.DateField()
	tob = models.CharField(max_length=12,null=True, blank=True)
	height = models.DecimalField(max_digits=2,decimal_places=1,null=True, blank=True)
	complexion = models.CharField(max_length=1,choices=COMPLEXION_CHOICES,null=True, blank=True)
	blood_group = models.CharField(max_length=1,choices=BLOOD_GROUP_CHOICES,null=True, blank=True)
	caste = models.CharField(max_length=30)
	birth_place = models.CharField(max_length=30,null=True, blank=True)
	qualification = models.CharField(max_length=100)
	course_hobbie = models.CharField(max_length=100,null=True, blank=True)
	occupation = models.CharField(max_length=30,null=True, blank=True)
	business = models.CharField(max_length=30,null=True, blank=True)
	agriculture = models.CharField(max_length=30,null=True, blank=True)
	house = models.CharField(max_length=50,null=True, blank=True)
	income = models.CharField(max_length=10,null=True, blank=True)
	#family-info
	father_occupation = models.CharField(max_length=30,null=True, blank=True)
	mother_occupation = models.CharField(max_length=30,null=True, blank=True)
	father_name = models.CharField(max_length=50,null=True, blank=True)
	father_nativeplace = models.CharField(max_length=50,null=True, blank=True)
	father_nativeplace_district = models.CharField(max_length=50)
	mother_nativeplace = models.CharField(max_length=50,null=True, blank=True)
	num_brothers = models.IntegerField(validators=[MinValueValidator(0),
                                      MaxValueValidator(10)],null=True, blank=True)
	num_brothers_married = models.IntegerField(validators=[MinValueValidator(0),
                                      MaxValueValidator(10)],null=True, blank=True)
	num_brothers_unmarried = models.IntegerField(validators=[MinValueValidator(0),
                                      MaxValueValidator(10)],null=True, blank=True)
	num_sisters = models.IntegerField(validators=[MinValueValidator(0),
                                      MaxValueValidator(10)],null=True, blank=True)
	num_sisters_married = models.IntegerField(validators=[MinValueValidator(0),
                                      MaxValueValidator(10)],null=True, blank=True)
	num_sisters_unmarried = models.IntegerField(validators=[MinValueValidator(0),
                                      MaxValueValidator(10)],null=True, blank=True)
	#expectations
	expectations = models.CharField(max_length=200,null=True, blank=True)

	#contact
	address = models.CharField(max_length=400,null=True, blank=True)
	address_district = models.CharField(max_length=400)
	phone = models.CharField(max_length=12,null=True, blank=True)
	mobile = models.CharField(max_length=12)

	#internal
	creator = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)



	def get_absolute_url(self):
		return reverse('matriaspirant-detail', kwargs={'pk': self.pk})


	def __str__(self):
		return	self.name



