from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

student_choice = [
	('لغات', 'لغات'),
	('عام', 'عام'),
	]

grade_choice = [
	('1s', 'اولي ثانوي'),
	('2s', 'تانية ثانوي '),
	('3s', 'تالتة ثانوي '),
	]
class CreateUserForm(UserCreationForm):
	first_name = forms.CharField( label= "full name ")
	ph = forms.CharField(label="phone number" )
	grade = forms.CharField(widget=forms.Select(choices=grade_choice))
	user_sort= forms.CharField( widget=forms.Select(choices=student_choice))
	class Meta:
		model = User
		fields = ['first_name' , 'username', 'password1', 'password2' ,'grade','ph' , 'user_sort' ]

	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['placeholder'] = 'الاسم كامل  '
		self.fields['password1'].widget.attrs['placeholder'] = ' كلمة السر   '
		self.fields['password2'].widget.attrs['placeholder'] = ' أعد كتابة كلمة السر'
		self.fields['username'].widget.attrs['placeholder'] = '  اسم المستخدم '
		self.fields['grade'].widget.attrs['placeholder'] = ' الصــف   '
		self.fields['ph'].widget.attrs['placeholder'] = '  رقم التليفون  '
		self.fields['user_sort'].widget.attrs['placeholder'] = ' عــام / لغــات   '


class searchForLastExamForm (forms.Form) :
	Exam_num = forms.IntegerField(label="Exam Number  "  )


