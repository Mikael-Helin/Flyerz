from django import forms
from .models import Event, EventComment

class EventForm(forms.ModelForm):
    # Make 'date' a date input field
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'event_flyer']


class EventCommentForm(forms.ModelForm):
    class Meta:
        model = EventComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',  
                'rows': 3,              
                'placeholder': 'Write your comment here...',
            }),
        }