from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

from .query_weather import get_weather
from django.conf import settings

# Create your views here.
@csrf_exempt
def webhook(request):
    response = MessagingResponse()
    if request.method == "POST":
        lat, lon = request.POST.get('Latitude'), request.POST.get('Longitude')
        if lat and lon:
            weather_response = get_weather(lat, lon, settings.OPEN_WEATHER_API_KEY)
        message = request.POST.get("Body")
        print(message)
        response.message('Rafiki, you said: ' + message)
    return HttpResponse(response.to_xml(), content_type='text/xml')