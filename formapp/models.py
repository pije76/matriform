from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator





GENDER_CHOICES=(('M','Male'),('F','Female'))
COMPLEXION_CHOICES=(('L','Light'),('F','Fair'),('W','Wheatish'),('D','Dark'))



class matriaspirant(models.Model):
	#personal info
	profilepic = models.ImageField("Profile Pic", upload_to="images/%Y/%m/%d", blank=False, null=True)
	name = models.CharField(max_length=50)
	gender = models.CharField(max_length=1,default='M',choices=GENDER_CHOICES)
	dob = models.DateField()
	tob = models.CharField(max_length=12)
	height = models.DecimalField(max_digits=2,decimal_places=1)
	complexion = models.CharField(max_length=1,default='L',choices=COMPLEXION_CHOICES)
	caste = models.CharField(max_length=30)
	birth_place = models.CharField(max_length=30)
	qualification = models.CharField(max_length=100)
	course_hobbie = models.CharField(max_length=100)
	occupation = models.CharField(max_length=30)
	business = models.CharField(max_length=30)
	agriculture = models.CharField(max_length=30)
	house = models.CharField(max_length=50)
	income = models.CharField(max_length=10)
	#family-info
	father_occupation = models.CharField(max_length=30)
	mother_occupation = models.CharField(max_length=30)
	father_name = models.CharField(max_length=50)
	father_nativeplace = models.CharField(max_length=50)
	mother_nativeplace = models.CharField(max_length=50)
	num_brothers = models.IntegerField(validators=[MinValueValidator(0),
                                      MaxValueValidator(10)])
	num_brothers_married = models.IntegerField(validators=[MinValueValidator(0),
                                      MaxValueValidator(10)])
	num_brothers_unmarried = models.IntegerField(validators=[MinValueValidator(0),
                                      MaxValueValidator(10)])
	num_sisters = models.IntegerField(validators=[MinValueValidator(0),
                                      MaxValueValidator(10)])
	num_sisters_married = models.IntegerField(validators=[MinValueValidator(0),
                                      MaxValueValidator(10)])
	num_sisters_unmarried = models.IntegerField(validators=[MinValueValidator(0),
                                      MaxValueValidator(10)])
	#expectations
	expectations = models.CharField(max_length=200)

	#contact
	address = models.CharField(max_length=400)
	phone = models.CharField(max_length=12)
	mobile = models.CharField(max_length=12)

	#internal
	creator = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)






	def __str__(self):
		return	self.name



