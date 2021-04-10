from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume
from django.views import View
# Create your views here.



class home(View):
    def get(self, request):
        form = ResumeForm()
        return render(request, 'resume/home.html', {  'form':form})
    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'resume/home.html', {'form':form})



def upload_pic(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'resume/home.html')
    else:
        form = ResumeForm()
        condidates=Resume.objects.all()
    return render(request, 'resume/home.html', {'form': form,'candidates':condidates})




class candidate(View):
    def get(self,request,pk):
        candidate=Resume.objects.get(pk=pk)
        return render(request,'resume/candidate.html',{'candidate':candidate})