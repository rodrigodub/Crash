from django.shortcuts import render, HttpResponse
from .models import HTVector

# Create your views here.
def home(request):
    # return HttpResponse('Physics Home Page')
    return render(request, 'Physics/home.html')

# vector list
def vector_list(request):
    # vlist = HTVector.objects.all()
    vlist = HTVector.objects.order_by('-id')
    context = {'vector_list': vlist}
    return render(request, 'Physics/vectors.html', context)

