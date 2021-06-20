from django.shortcuts import render
from main.models import Questions, user_answer,  user_info ,exam_info , submitted_user , user_score
from django import forms
from django.shortcuts import render, redirect
import re
from main.decorators import unauthenticated_user, allowed_users, admin_only
from main.forms import CreateUserForm , searchForLastExamForm
from django.contrib.auth.forms import UserCreationForm
import itertools
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


@unauthenticated_user
def registerPage(request):
	print(request.method)
	form = CreateUserForm()
	if request.method == 'POST':
		print(request.POST)
		form = CreateUserForm(request.POST)
		if form.is_valid():
			print ("iam here")
			user = form.save()
			username = form.cleaned_data.get('username')
			print(username)
			user_grade = form.cleaned_data.get('grade')
			user_phone = form.cleaned_data.get('ph')
			first_name = form.cleaned_data.get('first_name')
			user_sort = form.cleaned_data.get('user_sort')
			messages.success(request, 'Account was created for ' + username)
			query = user_info(user_id=username  , user_grade=user_grade  ,sort = user_sort,mobile=user_phone , first_name= first_name )
			query.save()
			return redirect('login3')
		else :
			return render(request , "main/login3.html" , {"form" : form})
	context = {'form': form}
	print(form.errors)
	return render(request, 'main/login3.html', context)


@unauthenticated_user
def loginPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			
			return redirect('quizview')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {'form': form}
	return render(request, 'main/login3.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login3')


def Quiz_view(request):
	
	if request.method == "POST":

		Add_Answers_toDB(request)
		return redirect("test_completed")
	
	else:
		

		user = get_user(request)
		

		current_exam = get_current_exam(request)
		if not current_exam :
			return redirect ("test_completed")
		else:
				# note here : iam in the last day of this project and here i want you to take care of something :
				#        	   here i check in user_answers if  (exam_id=current_exam.exam_num ) as i've done below in Add_Answers_toDB method 
				#   			q = user_answer( ...... , exam_id=  current_exam.exam_num , ........ )
				# 				don't ask me why i did it ....
				he_submitted_before = user_answer.objects.filter(user_id = user , exam_id=current_exam.exam_num)
				if he_submitted_before:
					return render (request , "main/test_completed.html" , {"NO_EXAM_Available" : "true"})
				
				else:
				
					send = Questions.objects.filter(exam_id = current_exam)
					return render(request , "main/quizview.html",{'content': send})
			


def get_current_exam(request):
	user = get_user(request)
	user_grade = user.user_grade
	print(user_grade)
	user_sort = user.sort
	current_exam = exam_info.objects.filter(grade_num = user_grade , sort = user_sort).last()
	return current_exam


def Add_Answers_toDB(request):

	user = get_user(request)

	first_name = user.first_name
	user_grade = user.user_grade

	fullName = first_name
	 	
	current_exam = get_current_exam(request)
	Ques_set = Questions.objects.filter(exam_id = current_exam.exam_id)

	score = 0 
	answers = []
	
	for i in request.POST :
		user_choice = request.POST.get(i , False)
		if user_choice =="c1" or  user_choice =="c2" or user_choice =="c3" or user_choice =="c4"  : 
			answers.append(user_choice)

	for user_choice , Ques in  zip (answers , Ques_set):

		if user_choice == "c1"  :
			if Ques.c1 == Ques.answer :
				score += Ques.marks
				q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = Ques.question_text , question_image =Ques.img,user_answers = Ques.c1 , correct_answer=Ques.answer  )
			else :
				q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = Ques.question_text , question_image =Ques.img,user_answers = Ques.c1 , correct_answer=Ques.answer , correct_way_toSolve=Ques.coorect_way)
			q.save()
			
			
		elif user_choice == "c2"  :
				if Ques.c2 == Ques.answer :
					score += Ques.marks
					q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = Ques.question_text , question_image =Ques.img,user_answers = Ques.c2 , correct_answer=Ques.answer )
				else:
					q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = Ques.question_text , question_image =Ques.img,user_answers = Ques.c2 , correct_answer=Ques.answer , correct_way_toSolve=Ques.coorect_way )
				q.save()
				
					
		elif user_choice == "c3"  :
				if Ques.c3 == Ques.answer :
					score += Ques.marks
					q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = Ques.question_text , question_image =Ques.img,user_answers = Ques.c3 , correct_answer=Ques.answer )
				else:
					q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = Ques.question_text , question_image =Ques.img,user_answers = Ques.c3 , correct_answer=Ques.answer , correct_way_toSolve=Ques.coorect_way )
				q.save()
				
					
		elif user_choice == "c4"  :
				if Ques.c4 == Ques.answer :
					score += Ques.marks
					q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = Ques.question_text, question_image =Ques.img ,user_answers = Ques.c4 , correct_answer=Ques.answer  )
				else:
					q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = Ques.question_text , question_image =Ques.img,user_answers = Ques.c3 , correct_answer=Ques.answer , correct_way_toSolve=Ques.coorect_way )
				q.save()
				
					
		else :
				q = user_answer(user_id = user, user_name = fullName ,exam_id=  current_exam.exam_num ,question_text = Ques.question_text, question_image =Ques.img ,user_answers = "NO ANSWER" , correct_answer=Ques.answer ,correct_way_toSolve=Ques.coorect_way )
				q.save()

	u = user_score(user_id= user , exam_id= current_exam ,exam_num = current_exam.exam_num ,FullName=fullName, score= score)
	u.save()

		
def get_user (request) :

	user_id = request.user.id
	user_name = User.objects.get(pk = user_id)
	user = user_info.objects.get(user_id=user_name)
	return user


def have_submitted(request , current_exam):
	user_id = request.user.id
	user_name = User.objects.get(pk = user_id)
	u = submitted_user.objects.filter(exam_id=current_exam.exam_id , user_id=user_name)
	if u :
		return True
	return False

def test_comp(request):
	user = get_user(request)
	first_name = user.first_name
	fullName = first_name
	current_exam = get_current_exam(request)
	if request.method == 'POST':

				exam_number = request.POST.get('exam_num')
				data = user_answer.objects.filter(exam_id= exam_number , user_id= user)
				
				if exam_exist(exam_number , user) :
					total_score = current_exam.total_score
					try :
						score = user_score.objects.get(exam_num=exam_number , user_id= user).score
					except:
						return render(request ,"main/test_completed.html", {"error" : "true"})
					contex = {"data_list": data ,
						"score" : score , 
						"Full_Name" : fullName ,
						"Exam_num" : exam_number ,
						"over_all" : total_score 
						}
					return render(request ,"main/test_completed.html", contex )

				else :

					return render(request ,"main/test_completed.html", {"not_such_exam" : "true"})

	else :

			
			if not current_exam :
				return render(request , "main/test_completed.html" , {"NO_EXAM_Available" : "true"})
			
			else :

				total_score = current_exam.total_score
				exam_num = current_exam.exam_num
				data = user_answer.objects.filter(exam_id= current_exam.exam_num , user_id= user)
				
				score = user_score.objects.get(exam_num= current_exam.exam_num  , user_id =user).score
				contex = {"data_list": data ,
						"score" : score , 
						"Full_Name" : fullName ,
						"Exam_num" : exam_num ,
						"over_all" : total_score 
						}

				return render(request , "main/test_completed.html" , contex)
			


def exam_exist(exam_number , user) :
	query = user_answer.objects.filter(user_id= user , exam_id= exam_number)
	if query :
		return True
	return False


		
def user_lastExams (request) :
	
	return render (request ,"main/user_exams.html"  )

def wiil_try (request) :
	return render (request ,"main/loginPage.html" )
