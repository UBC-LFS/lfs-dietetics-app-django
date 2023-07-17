from django.http import HttpResponse # Only for creating pages without a .html file
from django.shortcuts import render
from .models import ApplicationForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            formData = request.POST
            # valid cwl and student #??
            if (formData["studentEmail"] == formData["vertifyStudentEmail"] and formData["preferredEmail"] == formData["vertifyPreferredEmail"]):
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
    context = {
        "mandatoryQuestions": mandatoryQuestions,
        "optionalQuestions": optionalQuestions
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