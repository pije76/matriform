from django.db import models

GENDER_CHOICES=(('M','Male'),('F','Female'))



# http://stackoverflow.com/questions/8915296/python-image-library-fails-with-message-decoder-jpeg-not-available-pil

class matriaspirants(models.Model):
	profilepic = models.ImageField("Profile Pic", upload_to="images/", blank=True, null=True)
	name = models.CharField(max_length=50)
	gender = models.CharField(max_length=1,default='M',choices=GENDER_CHOICES)
	dob = models.DateField()
	address = models.CharField(max_length=400)
	phone = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

