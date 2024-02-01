from django.urls import path
from . import views

# Static Urls

'''urlpatterns = [
    path('january', views.january),
    path('february',views.february),
    path("march", views.march),
]'''


# Dynamic Urls based on logic on views.
# Passing string as Argument in views functions.
# Type castiing Path routers
urlpatterns = [
    path("",views.IntroPage),
    path("<int:month>",views.monthly_challenge_by_number),
    path("<str:month>",views.monthly_challenge, name = "month-challenge"),
]
