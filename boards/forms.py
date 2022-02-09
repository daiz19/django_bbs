from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
  message = forms.CharField(
    widget = forms.Textarea(
      attrs={'rows': 3, 'placeholder': 'Whats in your mind?'}
    ), 
    max_length=4000,
    help_text='The max lwngth of the text is 4,000.'
  )

  class Meta:
    model = Topic
    fields = ['subject', 'message']
