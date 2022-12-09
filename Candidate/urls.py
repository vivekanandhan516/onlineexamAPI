
from django.urls import path,include
from Candidate import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.log_view,name='login'),
    path('index/',views.index_view,name='index'),
    path('examview/',views.candidateexam,name='examview'),
    path('exam/<int:pk>/',views.test_view,name='exam'),
    path('results/',views.results,name='results'),
]
   
