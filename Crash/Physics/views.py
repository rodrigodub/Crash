from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import HTVector
from .forms import VectorFormMTheta, VectorFormXY

# Create your views here.
def home(request):
    # return HttpResponse('Physics Home Page')
    return render(request, 'Physics/home.html')


# vector list
def vector_list(request):
    # vlist = HTVector.objects.all()
    vlist = HTVector.objects.order_by('-id')

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        vformMT = VectorFormMTheta(request.POST)
        vformXY = VectorFormXY(request.POST)
        # check whether it's valid:
        if vformMT.is_valid():
            # process the data in form.cleaned_data as required
            vformMT.save(commit=True)
            # take the last vector and recalculate
            a = HTVector.objects.all()[len(HTVector.objects.all())-1]
            a.calculate()
            a.save()
            # redirect to a new URL:
            return render(request, 'Physics/home.html')
        elif vformXY.is_valid():
            # process the data in form.cleaned_data as required
            vformXY.save(commit=True)
            # take the last vector and recalculate
            a = HTVector.objects.all()[len(HTVector.objects.all())-1]
            a.calculate()
            a.save()
            # redirect to a new URL:
            return render(request, 'Physics/home.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        vformMT = VectorFormMTheta()
        vformXY = VectorFormXY()

    context = {'vector_list': vlist, 'vector_formMT': vformMT, 'vector_formXY': vformXY}

    return render(request, 'Physics/vectors.html', context)


# individual vector
def vector_num(request, id):
    vector = get_object_or_404(HTVector, pk=id)
    return render(request, 'Physics/vector_detail.html', {'vector': vector})