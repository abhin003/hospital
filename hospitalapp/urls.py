from django.urls import path
from hospitalapp import views

urlpatterns=[
path('',views.index),
path('about/',views.about),
path('contact/',views.contact),
path('gallery/',views.gallery),
path('service/',views.service),
path('single/',views.single),
path('docreg/',views.docreg),
path('doclogin/',views.doclogin),
path('patientreg/',views.patientreg),
path('patientlogin/',views.patientlogin),
path('booking/',views.booking),
path('logout/',views.logout),
path('book/',views.book),
path('frgpass/',views.newpass),
path('passconfirm/',views.confirm),
path('patmail/',views.patmail),
path('patpass/',views.passpat),
path('datta/',views.tabledata),












]