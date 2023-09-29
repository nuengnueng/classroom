from django import forms

class StudentScore(forms.Form):
    #id
    name = forms.CharField()
    course = forms.CharField()
    score = forms.IntegerField()