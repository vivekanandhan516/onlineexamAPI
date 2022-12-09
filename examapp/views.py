
from django.shortcuts import render,redirect
from .models import Exam,Question,exam_question
from .forms import ExamForm,QuestionForm,exam_question_Form
import time
import datetime	





def Exam_view(request):
	if request.method == 'POST':
		form = ExamForm(request.POST)
		if form.is_valid():
			form.save()
	form=ExamForm()
	return render(request,'examapp/view.html',{'form':form})

def Question_view(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			form.save()
	form=QuestionForm()
	return render(request,'examapp/view.html',{'form':form})
	
def exam_question_view(request):
	if request.method == 'POST':
		form = exam_question_Form(request.POST)
		if form.is_valid():
			form.save()
	form=exam_question_Form()
	return render(request,'examapp/view.html',{'form':form})
	


"""
def employeedata(req):
	user=User.objects.all()	
	return render(req,'examapp/view.html',{'user':user}) 
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
#            messages.success(request, "Successfully saved")
            return  redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'examapp/register.html', {'form': form})	

     

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
#            student = Student.objects.all()
            ur = form.cleaned_data['username']
            pd = form.cleaned_data['password']
            dbuser = User.objects.filter(user=ur, password=pd)
            if not dbuser:
#            	messages.success(request, "Successfully saved")
            	return  redirect('login')
            else:
                return  redirect('view')
    else:
        form = LoginForm()
        return render(request, 'examapp/login.html', {'form': form})

def Edit(request,use_id):
	empy=User.objects.get(pk=use_id)
	form=EditProfileForm(request.POST or None,instance=empy)
	if form.is_valid():
		form.save()
		return redirect('view')	
	return render(request,'examapp/update.html',{'form':form})
def delete(request,use_id):
	empy=User.objects.get(pk=use_id)
	empy.delete()	
	return redirect('view')
"""
       
    
		
