from django.template import Context, loader
from django.http import HttpResponse

def index(req):
	template = loader.get_template('index.html')

	
	context = Context({
		
	})

	return HttpResponse(template.render(context))
