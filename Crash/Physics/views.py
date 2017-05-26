from django.shortcuts import render, HttpResponse, redirect
from .models import HTVector
from .forms import VectorForm

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
        vform = VectorForm(request.POST)
        # check whether it's valid:
        if vform.is_valid():
            # process the data in form.cleaned_data as required
            # RODRIGO: DO SOMETHING AND TEST
            #a = HTVector(name=vform.fields['vectorInputName'], m=vform.fields['vectorMagnitude'], theta=vform.fields['vectorAngle'], x=vform.fields['vectorX'], y=vform.fields['vectorY'])
            vform.save(commit=True)
            # redirect to a new URL:
            return render(request, 'Physics/home.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        vform = VectorForm()

    context = {'vector_list': vlist, 'vector_form': vform}

    return render(request, 'Physics/vectors.html', context)

