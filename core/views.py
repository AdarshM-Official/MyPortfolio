from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from .forms import ContactForm

# Create your views here.
def home(request):
    context = {

        "projects": Project.objects.filter(featured=True),
        "experiences": Experience.objects.all(),
        "educations": Education.objects.all(),
        "services": Service.objects.all(),
        "skills": Skill.objects.all(),
    }
    return render(request, 'home2.html', context)

def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():

            ContactMessage.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                subject=form.cleaned_data["subject"],
                message=form.cleaned_data["message"],
            )

            return JsonResponse({
                "success": True,
                "message": "Message sent successfully."
            })

    return JsonResponse({
        "success": False
    })
