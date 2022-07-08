from django.shortcuts import render
from questions.models import Question
from answers.models import Answer
from .models import ChatLog, User
from company.models import Company

from .forms import ChatForm
# Create your views here.
def home(request):
    context = {}
    previous_data = None
    chat_form = ChatForm(request.POST or None)
    context['form'] = chat_form
    if chat_form.is_valid():
        user_id = chat_form.cleaned_data.get('user_id')
        text = chat_form.cleaned_data.get('text')
        print(user_id, text) 
        user = User.objects.get(pk=user_id)
        
        if text in ['hi', 'send announce ment']:
            
            message = Question.objects.get_defaut_message()
            print(message)
            
            #message.sent()
            context['object'] = message
            obj = ChatLog.objects.create(user=user, user_text_recived_body=text, sent_question=message)
        else:
            previous_data = ChatLog.objects.filter(user=user).order_by('-id').first()
        
        if previous_data:
            question = previous_data.sent_question or None
            answer = previous_data.sent_answer or None
            
            if question:
                message = Answer.objects.get(question=question, that_question_s_answer_number=text)
                
                #message.sent()
                context['object'] = message
                
                obj = ChatLog.objects.create(user=user, user_text_recived_body=text, sent_answer=message)
                
            else:
                message = Answer.objects.get(answer=answer, that_question_s_answer_number=text)
                
                context['object'] = message
                
                obj = ChatLog.objects.create(user=user, user_text_recived_body=text, sent_answer=message)
            
            
            
        
            
        context['form'] = chat_form
        
    return render(request, "home.html", context=context)