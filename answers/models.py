from django.db import models
from questions.models import Question

class AnswerManager(models.Manager):
    
    def get_defaut_message(self):
        return self.model.get(id=1)


# Create your models here.
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    that_question_s_answer_number = models.IntegerField()
    
    answer = models.ForeignKey("Answer", related_name='parent_answer', on_delete=models.CASCADE, null=True, blank=True)
    
    text = models.TextField()
    
    objects = AnswerManager()
    
    def __str__(self):
        return f"{'answer' if self.answer else 'question'} {self.answer.pk if self.answer else self.question.pk}'s answer number {self.that_question_s_answer_number}"
    
    @property
    def get_defaut_question(self):
        return self.model.objects.get(id=-1)