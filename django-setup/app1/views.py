from django.shortcuts import render,HttpResponse # type: ignore
from django.template import loader # type: ignore
from .models import SoilmoistureReading

# Create your views here.
def index(request):
    moisture_level = SoilmoistureReading.objects.all().values()
    template = loader.get_template('soil_moisture_list.html')
    context = {
        'moisture_level': moisture_level,
    }
    return HttpResponse(template.render(context,request))
