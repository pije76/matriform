from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

GENDER_CHOICES=(('M','Male'),('F','Female'))




class matriaspirants(models.Model):
	profilepic = models.ImageField("Profile Pic", upload_to="images/%Y/%m/%d", blank=False, null=True)
	name = models.CharField(max_length=50)
	gender = models.CharField(max_length=1,default='M',choices=GENDER_CHOICES)
	dob = models.DateField()
	# tob = models.TimeField(null=True)
	tob = models.CharField(max_length=12)
	address = models.CharField(max_length=400)
	phone = models.CharField(max_length=12)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return	self.name

