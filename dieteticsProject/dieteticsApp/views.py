from django.shortcuts import render
from .models import ApplicationForm

# Create your views here.
def index(request):
    form = ApplicationForm()
    context = {
        "form": form
    }
    return render(request, "form.html", context=context)