

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse


@csrf_exempt
def webhook(request):
    response = MessagingResponse()
    if request.method == "POST":
        message = request.POST.get("Body")
        print(message)
        response.message('You said: ' + message)
    return HttpResponse(response.to_xml(), content_type='text/xml')