from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'employee/index.html')

def query(request):
    return render(request,'employee/Query.html')