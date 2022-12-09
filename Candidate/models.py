from django.db import models
from examapp.models import Exam,Question,exam_question
from django.contrib.auth.models import User

class candidate(models.Model):
	user = models.ForeignKey(User,null = True,on_delete = models.CASCADE)
	name = models.CharField(max_length=20,null = True)
	mobile = models.IntegerField(null = True)
	email = models.EmailField(max_length = 100,null = True)
	created_at = models.DateTimeField(auto_now_add =True,null = True)
	modified_at = models.DateTimeField(auto_now=True,null = True)
    
class candidate_exam(models.Model):
	candidate=models.ForeignKey(candidate, on_delete=models.CASCADE,null =True)
	exam=models.ForeignKey(Exam, on_delete=models.CASCADE,null =True)
	num_attempted_questions=models.IntegerField(null = True,default =0)
	num_correct_questions=models.IntegerField(null = True,default =0)
	num_incorrect_questions=models.IntegerField(null = True,default =0)
	total_marks=models.IntegerField(null = True,default =0)

	
class candidate_exam_questions(models.Model):
	candidate=models.ForeignKey(candidate, on_delete=models.CASCADE,null =True)
	exam=models.ForeignKey(Exam, on_delete=models.CASCADE,null =True)
	question=models.ForeignKey(Question, on_delete=models.CASCADE,null =True)
	is_correct = models.BooleanField(null = True,default = False)
	marks = models.IntegerField(null = True,default = 0)
	is_attempted = models.BooleanField(default = False,null =True)











