from django.db import models


        
class Exam (models.Model):
	exam_date=models.DateField(auto_now_add=True,null = True)
	start_time = models.TimeField(auto_now_add=True,null = True)
	end_time = models.TimeField(auto_now_add=True,null = True)
	duration = models.DurationField(default='00:00:00',null = True)
	num_questions = models.IntegerField(default=0,null = True)
	maximum_marks= models.IntegerField(default=0,null = True)
	question_marks = models.IntegerField(null = True)
	question_negative_marks = models.IntegerField(null = True)
class Question(models.Model):
	question = models.TextField(max_length=500)
	option1 = models.CharField(max_length=100)
	option2 = models.CharField(max_length=100)
	option3 = models.CharField(max_length=100)
	option4 = models.CharField(max_length=100)
	choose = (('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4'))
	answer = models.CharField(max_length=1, choices=choose)
	
class exam_question(models.Model):
	exam=models.ForeignKey(Exam, on_delete=models.CASCADE,null = True)
	question=models.ForeignKey(Question, on_delete=models.CASCADE,null = True)     
  
