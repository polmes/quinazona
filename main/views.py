from django.http import HttpResponse
from django.template import loader
from .models import Station

# Create your views here.
def index(request):
	stations = Station.objects.all()
	context = {
		'stations': stations,
	}
	template = loader.get_template('main/index.html')
	return HttpResponse(template.render(context, request))
