from django.shortcuts import render
import re
from datetime import datetime
# Create your views here.
from django.http import HttpResponse

# def home(request):
    # Replace the existing home function with the one below
def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")
    # return HttpResponse("Hello, Django!")
def hello_there(request, name):
    # now = datetime.now()
    # formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    # match_object = re.match("[a-zA-Z]+", name)

    # if match_object:
    #     clean_name = match_object.group(0)
    # else:
    #     clean_name = "Friend"

    # content = "Hello there, " + clean_name + "! It's " + formatted_now
    # return HttpResponse(content)
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )