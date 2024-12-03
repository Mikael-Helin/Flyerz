from django import forms
from .models import Event, EventComment

class EventForm(forms.ModelForm):

    # make date a date input field
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'event_flyer']

class EventCommentForm(forms.ModelForm):
    class Meta:
        model = EventComment
        fields = ['content']