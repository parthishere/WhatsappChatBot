from django.db import models

from company.models import Company

class QuestionManager(models.Manager):
    
    def get_defaut_message(self):
        return self.model.objects.get(id=1)

# Create your models here.
class Question(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    
    question_text = models.TextField()
    
    objects= QuestionManager()
    
    def __str__(self):
        return f"company {self.company}'s question no {self.pk}"