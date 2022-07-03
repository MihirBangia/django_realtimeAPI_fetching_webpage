from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="indexfile"),
    path('sports',views.sports,name="sports"),
    path('entertainment',views.entertainment,name="entertainment"),
    path('technology',views.technology,name="technology"),
    path('buisness',views.buisness,name="buisness"),
    path('politics',views.politics,name="politics"),
]