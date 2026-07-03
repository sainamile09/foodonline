from django.shortcuts import render

# Create your views here.

def vProfile(request):
    return render(request,'accounts/vendor/vProfile.html')