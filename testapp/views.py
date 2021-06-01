from django.shortcuts import render
from testapp.models import Filter
# Create your views here.
#timesince_in_date_paramter_as_a_filtername
def filter(request):
    my_dict=Filter.objects.all()
    return render(request,'testapp/base.html',{'my_dict':my_dict})