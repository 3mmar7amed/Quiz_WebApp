from django.shortcuts import render
from main.models import Questions, user_answer,  user_info ,exam_info , submitted_user , user_score
from django import forms
from django.shortcuts import render, redirect
import re
from main.decorators import unauthenticated_user, allowed_users, admin_only
from main.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + username)
			user_grade = form.cleaned_data.get('grade')
			user_phone = form.cleaned_data.get('ph')
			first_name = form.cleaned_data.get('first_name')
			last_name = form.cleaned_data.get('last_name')
			query = user_info(user_id=username  , user_grade=user_grade  ,mobile=user_phone , first_name= first_name , last_name=last_name)
			query.save()
			return redirect('login')
	context = {'form': form}
	return render(request, 'main/register.html', context)


@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			
			return redirect('quizview')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'main/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


def Quiz_view(request):
	
	if request.method == "POST":
		Add_Answers_toDB(request)
		user_id = request.user.id
			
		user_name = User.objects.get(pk = user_id)
		print(user_name)
		user_grade = user_info.objects.get(user_id=user_name).user_grade
		current_exam = exam_info.objects.filter(grade_num= user_grade).last()
		data = Questions.objects.filter(exam_id= current_exam)
		return redirect(request, "main/test_completed.html", {"data_list": data})
	
	else:
		
			user_id = request.user.id
			
			user_name = User.objects.get(pk = user_id)
			print(user_name)
			user = user_info.objects.get(user_id=user_name)
			user_grade = user.user_grade
			
			current_exam = exam_info.objects.filter(grade_num = user_grade ).last()

			user_history = user_answer.objects.filter(user_id=user).last()
			print(user_history)
			
			if user_history and  user_history.exam_id == current_exam.exam_id :
				print("dddddddd")
				return render (request , "main/quizview.html") 
			
			else:
				send = Questions.objects.filter(exam_id = current_exam.exam_id)
				print (send)
				return render(request , "main/quizview.html",{'content': send}) 
		
		

def Add_Answers_toDB(request):

	user_id = request.user.id
	user_name = User.objects.get(pk = user_id)

	user = user_info.objects.get(user_id=user_name)

	first_name = user_info.objects.get(user_id=user_name).first_name
	last_name = user_info.objects.get(user_id=user_name).last_name
	user_grade = user_info.objects.get(user_id=user_name).user_grade

	fullName = "%s  %s" % (first_name,last_name)
	 	
	current_exam = exam_info.objects.filter(grade_num = user_grade).last()
	Ques_set = Questions.objects.filter(exam_id = current_exam.exam_id)

	score = 0 
	for (i,y) in zip(request.POST , Ques_set): 
		print(type(y))
		user_choice = request.POST.get(i , False)
		if user_choice == "c1":
			q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = y.question_text ,user_answers = y.c1 , correct_answer=y.answer )
			q.save()
			if y.c1 == y.answer :
				score += y.marks
		elif user_choice == "c2":
			q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = y.question_text ,user_answers = y.c2 , correct_answer=y.answer )
			q.save()
			if y.c2 == y.answer :
				score += y.marks
		elif user_choice == "c3":
			q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = y.question_text ,user_answers = y.c3 , correct_answer=y.answer )
			q.save()
			if y.c3 == y.answer :
				score += y.marks
	   
		elif user_choice == "c4":
			q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = y.question_text ,user_answers = y.c4 , correct_answer=y.answer )
			q.save()
			if y.c4 == y.answer :
				score += y.marks
		else :
			q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = y.question_text ,user_answers = "NO ANSWER" , correct_answer=y.answer )
			q.save()
		
		u = user_score(user_id= user , exam_id= current_exam ,FullName=fullName, score= score)
		u.save()
	
def have_submitted(request , current_exam):
	user_id = request.user.id
	user_name = User.objects.get(pk = user_id)
	u = submitted_user.objects.filter(exam_id=current_exam.exam_id , user_id=user_name)
	if u :
		return True
	return False

def test_comp(request):
	return render(request , "main/test_completed.html")

def base (request) :
	return render (request , "main/main.html")
