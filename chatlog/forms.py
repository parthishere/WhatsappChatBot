from django import forms

class ChatForm(forms.Form):
    
    user_id = forms.CharField(max_length=100)
    text = forms.CharField(max_length=100)
