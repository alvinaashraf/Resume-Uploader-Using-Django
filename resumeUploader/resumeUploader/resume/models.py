from django.db import models

# Create your models here.

STATE_CHOICES=(

    ('karachi','karachi'),
    ('Hyderabad	','Hyderabad'),
    ('Karachi South','Karachi South'),
    ('Malir','Malir'),
    ('Korangi','Korangi	')
)



class Resume(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=50)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=43)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices= STATE_CHOICES, max_length=24)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=60)
    profile_image=models.ImageField(upload_to='images/' , blank=True)
    my_file=models.FileField(upload_to='doc' , blank=True)










