
from django.contrib import admin
from django.urls import path
from examapp import views


urlpatterns = [
   path('view/', views.Exam_view),
   path('Ques/', views.Question_view),
   path('qe/', views.exam_question_view),
   
   
	
]

                          
                          
                          
                          
                          
                          
                          
                          
                          
