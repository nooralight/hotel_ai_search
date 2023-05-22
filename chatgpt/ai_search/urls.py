from django.urls import path
from . import views

urlpatterns=[
    path("",views.get_answer,name="ai_answer"),
    #path("get_result",views.get_answer,name="ai_answer"),
]
