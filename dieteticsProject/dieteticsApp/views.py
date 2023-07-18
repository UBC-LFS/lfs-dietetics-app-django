from django.http import HttpResponse # Only for creating pages without a .html file
from django.shortcuts import render
from .models import Constants
from .forms import ApplicationForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            formData = request.POST
            # valid cwl and student #??
            if (formData["studentEmail"] == formData["vertifyStudentEmail"] and formData["preferredEmail"] == formData["vertifyPreferredEmail"]):
                # Save to database
                form.save()
                return HttpResponse("<p>Thanks! Your application has been submitted!</p>")
        else:
            print(form.errors)
    
    else:
        form = ApplicationForm()

    mandatoryQuestions = []
    optionalQuestions = []
        
    for input in form:
        if ("aboriginal" in input.name):
            optionalQuestions.append(input)
        else:
            mandatoryQuestions.append(input)
    
    try:
        for constant in Constants.objects.all():
            if (str(constant) == "year"):
                year = constant.value
    except:
        pass
            
    # If no year found from constants
    if 'year' not in locals():
        year = "(YEAR UNDEFINED)" 

    context = {
        "mandatoryQuestions": mandatoryQuestions,
        "optionalQuestions": optionalQuestions,
        "year": year
    }
    return render(request, "form.html", context=context)

# def submitApp(request):
#     if request.method == "POST":
#         form = ApplicationForm(request.POST)
#         if form.is_valid():
#             return HttpResponse("<p>Thank!</p>")
#         else:
#             form = ApplicationForm()
#             print("ERROR")
#         return render(request, "form.html", {"form": form})