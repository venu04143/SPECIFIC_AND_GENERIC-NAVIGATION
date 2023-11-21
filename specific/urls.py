from specific.views import *
from django.urls import path

app_name='nothing'

urlpatterns=[
    path('sansa/',sansa,name='sansa'),
    path('arya/',arya,name='arya')

]