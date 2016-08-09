import json
import requests
import urlparse
from django_twilio.views import twilio_view
from twilio.twiml import Response
#from django.views.decorators.csrf import csrf_exempt
BASE_URL = 'http://pokeapi.co'

def query_p(resource_url):
    #url to be joined by urlparse
    url=urlparse.urljoin(BASE_URL,resource_url)
    response=requests.get(url)

    if response.status_code==200:
        #to load json data
        data=json.loads(response.text)
        return data
#@csrf_exempt
@twilio_view #install twilio-python and django-twilio for using twilio
def incoming_message(request):
    #since twilio takes http request from user
    twiml = Response() #store the request
    body = request.POST.get('Body', '')
    body = body.lower()

    res='/api/v1/pokemon/%s/' % (body)
    pokemon = query_p(res)

    if pokemon:
        sprite_uri = pokemon['sprites'][0]['resource_uri']
        description_uri = pokemon['descriptions'][0]['resource_uri']

        sprite = query_p(sprite_uri)
        description = query_p(description_uri)

        message = '{0}, {1}'.format(pokemon['name'], description['description'])
        image = urlparse.urljoin(BASE_URL, sprite['image'])

        #frm = request.POST.get('From', '')
        #if '+12' in frm:
        #    twiml.message('{0} {1}'.format(message, image))
        #    return twiml
        #twiml.message(message).media(image)
        #return twiml
#https://www.twilio.com/docs/api/twiml read for twiml functions like body,media,message etc.
    twiml.message("Something went wrong! Try 'Pikachu' or 'Rotom'")
    return twiml
