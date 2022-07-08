from django.db import models

from questions.models import Question
from answers.models import Answer
from django.contrib.auth.models import User

# Create your models here.
class ChatLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    user_text_recived_body = models.CharField(max_length=100, null=True, blank=True)
    
    sent_question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    sent_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.answer_id if self.answer_id else self.question_id} sent to {self.user_id} user "