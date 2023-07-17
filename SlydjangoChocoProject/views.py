from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return  render(request,'about.html')

def testmonial(request):
    return render(request,'testimonial.html')

def choco(request):
    return render(request,'chocolate.html')
