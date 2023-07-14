from django.shortcuts import render
from .models import ApplicationForm

# Create your views here.
def index(request):
    form = ApplicationForm()
    mandatoryQuestions = []
    optionalQuestions = []
    
    for input in form:
        if ("aboriginal" in input.name):
            optionalQuestions.append(input)
        else:
            mandatoryQuestions.append(input)
    context = {
        "mandatoryQuestions": mandatoryQuestions,
        "optionalQuestions": optionalQuestions
    }
    return render(request, "form.html", context=context)