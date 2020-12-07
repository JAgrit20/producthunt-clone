from django.shortcuts import render

# Create your views here.
def homeacc(request):
    return render(request,'accounts/homeacc.html')