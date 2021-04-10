from django import forms
from .models import Resume


GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]
JOB_CITY_CHOICE=[
    ('Karachi','Karachi'),
    ('Lahore','Lahore'),
    ('Punjab','Punjab'),
    ('Hyderabad','Hyderabad')
]


class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect())
    job_city=forms.MultipleChoiceField(label="Preferred Job Location",choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields=['name','dob','email','gender','locality','city','pin','state','mobile','job_city','profile_image','my_file']
        labels={'name':'Full Name','dob':'Date of Birth','email':'Email Address','pin':'Pin Code','mobile':'Mobile Number','profile_image':'Profile Image','my_file':'Document'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),




        }


