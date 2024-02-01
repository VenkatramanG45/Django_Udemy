from calendar import month
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound ,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january" : "Eat no meat for the entire month !",
    "february" : "Walk for at least 20 minutes every day !",
    "march" : "Learn Django for 20 minutes everyday !",
    "april" : "Eat no meat for the entire month !",
    "may" :  "Walk for at least 20 minutes every day !",
    "june" :  "Learn Django for 20 minutes everyday !",
    "july" : "Eat no meat for the entire month !",
    "august" : "Walk for at least 20 minutes every day !",
    "september" : "Learn Django for 20 minutes everyday !",
    "october" : "Eat no meat for the entire month !",
    "november" : "Walk for at least 20 minutes every day !",
    "december" : None,
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html",{
       "months" : months 
    })



def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
        #return Http404()







