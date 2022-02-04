from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

dict={
    'january' : "Learn Django",
    'february' : "Walk 10 km",
    'march' : None,
    'april' : "Cook Pizza",
    'may' : "Go to Ghost House",
    'june' : "Sing a song",
    'july' : "Dance like a Joker",
    'august' : "Make a Pancake",
    'september' : "Read a book",
    'october' : None,
    'november' : "Buy a car",
    'december' : None
}

def index(request):
    months = list(dict.keys())
    return render(request,'challenges/index.html',{ 
        "months" : months,
    })

def monthly_challenge_by_number(request,month):
    months = list(dict.keys()) 
    try:
        redirect_month = months[month-1]
        redirect_path = reverse('monthly-challenge',args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        error_message = render_to_string('404.html')
        return HttpResponseNotFound(error_message)
    


def monthly_challenge(request,month):
    try:
        challenge_message=dict[month]
        # response_text = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_text)
        return render(request, 'challenges/challenge.html',{
            "text" : challenge_message,
            "month_name" : month
        })
    except:
        error_message = render_to_string('404.html')
        return HttpResponseNotFound(error_message)