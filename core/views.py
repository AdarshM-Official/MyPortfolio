from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    context = {

        "projects": Project.objects.filter(featured=True),
        "experiences": Experience.objects.all(),
        "educations": Education.objects.all(),
        "services": Service.objects.all(),
        "skills": Skill.objects.all(),
    }
    return render(request, 'hometest.html', context)
