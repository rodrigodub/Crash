from django.shortcuts import render, get_object_or_404
# from django.views.generic.edit import UpdateView
from django.urls import reverse
from .models import CCTransistor
from .forms import TransistorForm, TransistorFormUpdate

# Create your views here.
def computer_home(request):
    return render(request, 'Computer/computer_home.html')


def transistor_list(request):
    transistors = CCTransistor.objects.order_by('-id')
    # POST
    if request.method == 'POST':
        # post the contents of transForm form
        transForm = TransistorForm(request.POST)
        if transForm.is_valid():
            transForm.save(commit=True)
            # take the just created transistor and update() it to do the electronics
            lastTrans = CCTransistor.objects.all()[len(CCTransistor.objects.all())-1]
            lastTrans.update()
            lastTrans.save()
            # redirect to a new URL:
            return render(request, 'Computer/transistor_list.html'
                          , {'transistors': transistors, 'transistor_form': TransistorForm()})
    # GET
    else:
        transForm = TransistorForm()
        return render(request, 'Computer/transistor_list.html'
                      , {'transistors': transistors, 'transistor_form': TransistorForm()})


# class transistor_update(UpdateView):
#     model = CCTransistor
#     fields = ['electrode_in', 'gate']
#
#     def get_success_url(self):
#         return reverse('transistor_list')
#
#     def get_object(self, queryset=None):
#         # tran = CCTransistor.objects.get(id=self.kwargs['pk'])
#         tran = self.model.objects.get(pk=self.kwargs['pk'])
#         # tran.update()
#         return tran
#
#     def form_valid(self, form):
#         #form.instance.update()
#         form.get_object().update()
#         return super(transistor_update, self).form_valid(form)


def transistor_update(request, id):
    transistors = CCTransistor.objects.order_by('-id')
    theTransistor = get_object_or_404(CCTransistor, pk=id)
    # theTransistor = CCTransistor.objects.get(pk=id)
    # POST
    if request.method == 'POST':
        transForm = TransistorFormUpdate(request.POST or None, instance=theTransistor)
        if transForm.is_valid():
            transForm.save(commit=True)
            # theTransistor = CCTransistor.objects.get(pk=id)
            theTransistor.update()
            theTransistor.save()
            return render(request, 'Computer/transistor_list.html'
                          , {'transistors': transistors, 'transistor_form': TransistorForm()})
    # GET
    else:
        return render(request, 'Computer/transistor_update.html'
                      , {'transistor_update': TransistorFormUpdate(instance=theTransistor)})



