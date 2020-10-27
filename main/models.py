from django.db import models
from django.contrib.auth.models import User 



class user_info(models.Model):
	user_id= models.CharField(unique= True , primary_key=True , max_length= 300)
	first_name = models.CharField(max_length=300 , default="")
	last_name = models.CharField(max_length=300 , default= "")
	user_grade = models.IntegerField(default= 0)
	mobile = models.CharField(max_length=200 , default='')



class exam_info(models.Model):
	exam_id =  models.AutoField(primary_key=True)
	exam_num = models.IntegerField(default=0)
	grade_num = models.IntegerField(default=0)

class user_answer(models.Model):
	
	user_id = models.ForeignKey(
		user_info, on_delete=models.CASCADE )
	
	user_name = models.CharField(max_length=200)
	
	exam_id = models.IntegerField(default="")

	question_text = models.CharField(max_length=200)
	user_answers = models.CharField(max_length=200)
	correct_answer = models.CharField(max_length=200)
 

class Questions(models.Model):
	question_id = models.AutoField(primary_key=True)
	exam_id = models.ForeignKey( exam_info , on_delete=models.CASCADE )
	question_text = models.CharField(max_length=200)
	img = models.ImageField(upload_to='images/', null=True, blank=True )
	c1 = models.CharField(max_length=200, default='')
	c2 = models.CharField(max_length=200, default='')
	c3 = models.CharField(max_length=200, default='')
	c4 = models.CharField(max_length=200, default='')
	answer = models.CharField(max_length=200)
	marks = models.IntegerField()

	
class img (models.Model):
	img = models.ImageField(upload_to='images/', null=True, blank=True )

class submitted_user(models.Model):
	exam_id = models.IntegerField( primary_key=True )
	user_id = models.CharField( max_length= 300)

class user_score (models.Model) :
	score = models.IntegerField(default= 0)
	FullName = models.CharField(max_length=200, default='')
	exam_id = models.ForeignKey( exam_info , on_delete=models.CASCADE )
	user_id = models.ForeignKey(user_info, on_delete=models.CASCADE )

	