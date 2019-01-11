from django import forms
from .models import Members

#authorised members are in this form
class MemberForm(forms.ModelForm):
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={
                                   'placeholder':'Enter a password',
                               }))


    class Meta:
        model=Members
        fields=[
            'usn', 'pwd'
        ]

