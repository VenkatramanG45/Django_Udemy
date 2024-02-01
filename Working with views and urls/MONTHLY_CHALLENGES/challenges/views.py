#Working with Urls and Views

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound ,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# For static URLS


'''def index(request):
    return HttpResponse("This Work !")

def january(request):
    return HttpResponse("Eat no meat for entire month")

def february(request):
    return HttpResponse("Walk for at least 20 minutes everyday")

def march(request):
    return HttpResponse("Learn Django for 20 minutes everyday") '''
    
    
    
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
    "december" : "Learn Django for 20 minutes everyday !",
}

def IntroPage(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge" ,args = [month])
        list_items += f"<li><a href =\"{month_path}\">{month.capitalize()}</a></li>"
    """"
        <ul>
            <li><a href = "/challenges/january">January</a></li>
        <ul>
    """
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
    
    
    '''Intro = "Hi there! \n Ready for 1 year Challenge."
    return HttpResponse(f"<h1>{Intro}</h1>")'''
    
      
    
def  monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseRedirect("Invalid Month")
        
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge" ,args = [redirect_month])  # this args converts  number to respective month , the changes will be absorbed in URL.
    return HttpResponseRedirect(redirect_month) 
    

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        response_data =f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except: 
        return HttpResponseNotFound("<h1>This month is not supported !</h1>")
    
    
    '''if month == "january":
        challenge_text = "Eat no meat for entire month !"
    elif month =="february":
        challenge_text = "Walk for atleast 20 minutes a day !"
    elif month == "march":
        challenge_text = "Learn Django for atleast 20 minutes a day"
    else:
         return HttpResponseNotFound("This month is not supported")'''       
    
        
   