from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from listing.models import Listing
import mimetypes

# Create your views here.
def welcome(request):
    #return HttpResponse("This is a \"ToDo\" listing webapp, "+"Time of response: "+str(datetime.now())
    return render(request,"welcome.html",{"timestamp":str(datetime.now()),})

def about(request):
    start_msg = "<html lang=\"en\"><head><meta charset=\"UTF-8\"><title>About MD</title>"
    style_msg = "<link rel=\"stylesheet\" href=\"/static/style.css\"></head>"
    url1 = "<a href=\"https://www.linkedin.com/in/mohammed-hussain-669832129\" target=\"_blank\" rel=\"noopener noreferrer\">LinkedIn Profile</a>"
    url2 = "<a href=\"http://ieeexplore.ieee.org/abstract/document/8321253\" target=\"_blank\" rel=\"noopener noreferrer\">Algorithm Developed</a>"
    url3 = "<a href=\"https://github.com/MD101\" target=\"_blank\" rel=\"noopener noreferrer\">GitHub Profile</a>"
    Title = "<h2>About MD</h2>"
    Back = "<button type=\"submit\" onclick=\"location.href=\'/\'\">Return</button>"
    message = f"{start_msg}{style_msg}<body>{Title}To Contact Mohammed Please Find the urls for the same</br>LinkedIn Profile: {url1} </br>IEEE Project: {url2}</br>Github Profile: {url3} </br> {Back}</body>"
    return HttpResponse(message, content_type = "text/html")

def Descriptions(request, id):
    descripts = Listing.objects.get(pk=id)
    return render(request,"description.html",{"description":descripts})

def contactus(request):
    message ="There's Mohammed's Resume File already being downloaded on your device, If found interested forward it for employment accordingly, Thank you."
    response = HttpResponse(message, headers ={'Content-Type':'text/html','Content-Disposition': 'attachment; filename="/static/MohammedMuzaherHussain-v2-4-5.pdf"'})
    return response
