import random
from datetime import datetime

from django.http import HttpResponse # Only for creating pages without a .html file
from django.shortcuts import render
from .models import Constant, Application
from .forms import ApplicationForm

# Stores current applicant's application number so it remains the same on front + backend when submitting or if an error occurs
applicants = {

}

# Create your views here.
def index(request):
    try:
        for constant in Constant.objects.all():
            if (str(constant) == "applicationsOpen"):
                applicationsOpen = datetime.strptime(constant.value, '%Y-%m-%d')
            if (str(constant) == "applicationsClose"):
                applicationsClose = datetime.strptime(constant.value, '%Y-%m-%d')

        applicationsAreOpen = datetime.now() >= applicationsOpen and datetime.now() <= applicationsClose

    except:
        # default value if no applicationsOpen or applicationsClose constants declared
        applicationsAreOpen = False

    context = {
        "applicationsAreOpen": applicationsAreOpen
    }
    return render(request, "index.html", context=context)

def form(request):
    # redirect to login to cwl??
    # get cwl and shibSN?
    
    cwl = "bobl1" + str(random.randint(1,9))
    print(applicants)
    if (cwl in applicants):
        applicationNumber = applicants[cwl]
    else:
        # Create application number and verify that it is not being used
        applicationNumberUsed = True
        while applicationNumberUsed:
            applicationNumberUsed = False
            applicationNumber = random.randint(1000000, 3000000)
            for application in Application.objects.all():
                if (int(application.applicationNumber) == int(applicationNumber)):
                    applicationNumberUsed = True

        applicants[cwl] = applicationNumber

    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            formData = request.POST
            # valid cwl and student #??
            if (formData["studentEmail"] == formData["vertifyStudentEmail"] and formData["preferredEmail"] == formData["vertifyPreferredEmail"]):
                # Save to database
                applicant = Application()
                applicant.cwl = cwl
                applicant.applicationNumber = applicationNumber
                applicant.dateApplied = datetime.now()
                applicant.lastName = formData["lastName"]
                applicant.firstName = formData["firstName"]
                applicant.cei = formData["cei"]
                applicant.studentNumber = formData["studentNumber"]
                applicant.studentEmail = formData["studentEmail"]
                applicant.vertifyStudentEmail = formData["vertifyStudentEmail"]
                applicant.preferredEmail = formData["preferredEmail"]
                applicant.vertifyPreferredEmail = formData["vertifyPreferredEmail"]
                applicant.phoneNumber = formData["phoneNumber"]
                applicant.birthday = formData["birthday"]
                applicant.firstApp = formData["firstApp"]
                applicant.appTimesDropdown = formData["appTimesDropdown"]
                applicant.aboriginal = formData["aboriginal"]
                applicant.aboriginalChoices = formData["aboriginalChoices"]
                
                applicant.save()
          
                context = {
                    "applicationNumber": applicationNumber
                }
                return render(request, "confirmation.html", context=context)
        
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
        for constant in Constant.objects.all():
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
        "year": year,
        "applicationNumber": applicationNumber
    }
    return render(request, "form.html", context=context)