from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from Candidate.models import candidate,candidate_exam,candidate_exam_questions
from django.contrib import messages
from django.contrib.auth import authenticate,login
from rest_framework.response import Response
import jwt
import pytz
from datetime import datetime,timedelta
from datetime import date
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from .authorization import isAuthorized
from examapp.models import Exam,Question,exam_question


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        username=request.POST['email']
        email=request.POST['email']
        mobile =request.POST['mobile']
        password=request.POST['password']
        password1=request.POST['password1']

        if password == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request,'username already exist')
                return redirect('register')

            # elif User.objects.filter(email = email).exists():
            #     messages.info(request,'email already exist')
            #     return redirect('register')

            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name)
                user.save()
                user_details = User.objects.get(username = username) 
                user1 = candidate(email=email,name=first_name,mobile = mobile,user_id = user_details.id)
                user1.save()
                print("user created")
                return redirect('login')
        else:
            return redirect('register')
    else:    
        return render(request,"candidate/register.html")
def log_view(request):
	if request.method == "POST":
		username=request.POST['email']
		password=request.POST['password']
		user=authenticate(request,username=username, password=password )
		if user is not None:
			token=jwt.encode({'username':username,'password':password,
			'exp':datetime.utcnow()+timedelta(hours=24)},
			settings.SECRET_KEY,algorithm='HS256')
			request.session['Authorization'] =token
			return redirect('index')
		messages.success(request,("please give correct information"))
		return redirect('login')
	return render(request,"candidate/login.html") 
def index_view(request):
        user = isAuthorized(request)
        return render(request,"candidate/test2.html") 
def candidateexam(request):
    user_email = isAuthorized(request)
    today_date = date.today()
    timezone = pytz.timezone("Asia/Kolkata")
    time_now = datetime.now(tz=timezone).time()
    today_exam = Exam.objects.filter(exam_date = today_date).values()

    exam_ready_to_start =[]
    for exam in today_exam:
        if exam['start_time'] <= time_now and time_now <= exam['end_time'] :
            exam_ready_to_start.append(exam['id'])
    print(exam_ready_to_start,'available ids')
    context = {
                'today_exam':today_exam,
                'exam_ready_to_start':exam_ready_to_start,
            }
    return render(request,'candidate/test3.html',context)        
        
        
        
             		
def test_view(request,**kwargs): 
    user_email = isAuthorized(request)
    candidate_obj = candidate.objects.filter(email = user_email).first()
    exam_id = kwargs['pk']
    exam_details = Exam.objects.filter(id = exam_id).values()[0]
    exam_question_ids = list(exam_question.objects.values_list('question').filter(exam = exam_details['id']))
    ids=[]
    
    timezone = pytz.timezone("Asia/Kolkata")
    timenow = datetime.now(tz=timezone)
    print(timenow)
    duration = exam_details['duration']
    print(duration,"duration")
    alltimedelta=timedelta(hours=1)
    addtime= timenow + alltimedelta
    print(addtime)
    endtime = addtime.strftime("%m/%d/%Y, %H:%M:%S")

    exam_end = exam_details['end_time']
    today_date = date.today()
    exam_end_time=endtime
    exam_end_time = datetime.combine(today_date, exam_end)
    exam_end_time = exam_end_time.strftime("%m/%d/%Y, %H:%M:%S")
    print(exam_end_time,'end timeexam')
    exam_obj = Exam.objects.get(id=exam_id)

    check_candidate = candidate_exam.objects.filter(exam = exam_obj,candidate = candidate_obj).values()[0]
    if check_candidate == None:
        context = {
            'message': 'You already attend this quiz, Thank you!'
        }
    else:
        for i in exam_question_ids:
            ids.append(i[0])
        exam_questions = list(Question.objects.filter(id__in = ids).values())
        context = {
            'exam' : exam_details,
            'exam_questions' : exam_questions,
            'endtime'  : endtime,
            'exam_end_time':exam_end_time
        }


    if request.method == 'POST':

        for id in ids:
            question_id = id
            questionobj = Question.objects.filter(id = question_id).values()[0]
            quest_obj = Question.objects.get(id = question_id)
            answer = request.POST.get(str(id))
            if answer:
                is_attempted = True
                is_correct = True if questionobj['answer'] == answer else False
                if(is_correct == True):
                    mark = exam_details['question_marks']
                else:
                    mark = exam_details['question_negative_marks']
            else:
                is_attempted = False
                mark = 0
                is_correct = False
            answerObj = candidate_exam_questions.objects.create(candidate = candidate_obj, exam= exam_obj , question = quest_obj,is_correct = is_correct,marks = mark,is_attempted=is_attempted)
            answerObj.save()

        # Section For Candidate Quiz
        no_of_attempted = candidate_exam_questions.objects.filter(exam = exam_obj,candidate = candidate_obj,is_attempted = True).count()
        print(no_of_attempted,'attempted')
        no_of_correct_questions = candidate_exam_questions.objects.filter(exam = exam_obj,candidate = candidate_obj,is_correct = True).count()
        print(no_of_correct_questions,'corrct answer')
        #total_no_questions = quiz_details['num_of_questions]

        no_of_incorrect_questions = no_of_attempted - no_of_correct_questions
        print(no_of_incorrect_questions,'incorrect')
        total_mark = (no_of_correct_questions * exam_details['question_marks']) - (no_of_incorrect_questions * exam_details['question_negative_marks'])
        print(total_mark,'total mark')
        result = candidate_exam.objects.create(candidate = candidate_obj,exam = exam_obj,num_attempted_questions = no_of_attempted,num_correct_questions =no_of_correct_questions,num_incorrect_questions = no_of_incorrect_questions,total_marks = total_mark)
        result.save()
        return redirect('results')
    return render(request,'candidate/test.html',context)
def results(request):
    user_email = isAuthorized(request)
    print(user_email,'user name')
    if(user_email):
        candidate_obj = candidate.objects.filter(email = user_email).first()
        results = candidate_exam.objects.filter(candidate = candidate_obj)
    
    return render(request,'candidate/test4.html',{'results':results})
          	      
        
  
     
