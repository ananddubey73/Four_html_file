from django.shortcuts import render

# Create your views here.
def file1(request):
    return render(request,'file1.html')

def file2(request):
    return render(request,'file2.html')

def file3(request):
    return render(request,'file3.html')

def file4(request):
    return render(request,'file4.html')

