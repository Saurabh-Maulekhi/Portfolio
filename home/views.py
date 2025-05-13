from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable1":"wow1"
    }
    return render(request, 'index.html',context)
    # return HttpResponse("this is home")

def about(request):
    return HttpResponse("this is about")

def projects(request):
    return HttpResponse("these are projects")

def contact(request):
    return HttpResponse("this is contact")