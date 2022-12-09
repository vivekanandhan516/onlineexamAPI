
from django import forms
from .models import Exam,Question,exam_question


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = [ 'duration', 'num_questions', 'maximum_marks','question_marks','question_negative_marks']
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['question','option1','option2','option3','option4','answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})     
            } 
        
class exam_question_Form(forms.ModelForm):
    class Meta:
        model = exam_question
        fields = ['exam','question']
        
                                      
