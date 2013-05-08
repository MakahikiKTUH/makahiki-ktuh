'''
Created on Apr 16, 2013

@author: shindig
'''
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from apps.widgets.projects.models import Goal 

YEAR_CHOICES = ('2013', '2014')

class ProjectForm(forms.Form):
    title = forms.CharField(max_length=75)
    short_description = forms.CharField(max_length=300)
    long_description = forms.CharField(widget=forms.Textarea)
    number_of_members = forms.IntegerField(max_value=100, min_value=1)
    deadline = forms.DateField(widget=SelectDateWidget(years=YEAR_CHOICES))


class GoalForm(forms.ModelForm):
    text = forms.CharField(max_length=300, required=False)
    deadline = forms.DateField(widget=SelectDateWidget(years=YEAR_CHOICES), required=False)

    class Meta:
        model = Goal
        fields = ('deadline', 'text')
        widgets = {'deadline': SelectDateWidget(years=YEAR_CHOICES),}

    def has_no_text_or_deadline(self):
        has_text_or_deadline = False
        data = self.cleaned_data['text']
        if data != "" or data is not None:
            has_text_or_deadline = True
        data = self.cleaned_data['deadline']
        if data != "" or data is not None:
            has_text_or_deadline = True
        return has_text_or_deadline

class GoalForm2(forms.Form):
    deadline = SelectDateWidget(years=YEAR_CHOICES)
    text = forms.Textarea

class CommentForm(forms.ModelForm):
    class Meta:
        exclude = ('project', 'created', 'player')