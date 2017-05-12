from django.shortcuts import render
from django.http import HttpResponse
from .models import news
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import re
import base64
# Create your views here.
def index(request):
	news_list = news.objects.all()
	template = loader.get_template('news/index.html')
	context = {'news_list':news_list}
	return HttpResponse(template.render(context,request))
def games(request,value):
	return HttpResponse("The value sent is %s"%value)
def politics(request,value,value2):
	return HttpResponse("The value is %s"%value %value2)
def camera(request):
	print ('Inside camera.html')
	return render(request,'news/camera.html')
@csrf_exempt
def upload(request):
	dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
	ImageData = request.POST.get('image')
	ImageData = dataUrlPattern.match(ImageData).group(2)
	if(ImageData == None or len(ImageData) == 0):
		print('Goodbye, cruel world!')
	ImageData = base64.b64decode(ImageData)
	print ('Goodbye, sadsa!')
	return HttpResponse("Uploaded to backend")