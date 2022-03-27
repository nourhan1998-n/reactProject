from django.shortcuts import render
from .models import certificates,clients,footer,ownedCompanies,aboutUs,seaJob,landJob
# Create your views here.
def home(request):
    about=aboutUs.objects.all()
    return render(request,'index.html',{'about':about})

def job(request):
    return render(request,'job.html')


