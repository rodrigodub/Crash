from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('Physics Home Page')
    return render(request, 'Physics/index.html')
