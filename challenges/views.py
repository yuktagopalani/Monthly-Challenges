from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

dict={
    'january' : "This is january month",
    'february' : "This is february month"
}

def monthly_challenge_by_number(request,month):
    months = list(dict.keys()) 
    try:
        redirect_month = months[month-1]
        redirect_path = reverse('monthly-challenge',args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound('<h1>Invalid</h1>')
    


def monthly_challenge(request,month):
    try:
        text=dict[month]
        response_text = f"<h1>{text}</h1>"
        return HttpResponse(response_text)
    except:
        return HttpResponseNotFound('<h1>Invalid</h1>')