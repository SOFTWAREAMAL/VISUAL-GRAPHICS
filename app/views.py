from django.shortcuts import render,redirect
from .models import SampleData
import json


def chart(request):
    data = SampleData.objects.all().values('name','value')
    data_json = json.dumps(list(data))
    print(data_json)
    return render(request,'chart.html',{'data':data_json})


def create(request):
    if request.method == "POST":
        name = request.POST['name']
        value = request.POST['value']

        data = SampleData(name=name,value=value)
        data.save()
        return redirect('chart_view')
    return render(request,'data.html')