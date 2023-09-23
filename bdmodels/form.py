from django import forms

class Personforma(forms.Form):
    name1 = forms.CharField(max_length=10)
    age1 = forms.IntegerField(max_value=120, min_value=1)