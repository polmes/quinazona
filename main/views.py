from django.shortcuts import render
from .models import Station

# Create your views here.
def index(request):
	stations = Station.objects.all()
	context = {
		'stations': stations,
	}
	return render(request, 'main/index.html', context)
