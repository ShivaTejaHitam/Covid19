from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns=[
    path('beds/',views.homepage,name="homepage"),
    path('ventilators/',views.homepage2,name="homepage2"),
    path('isolationwards/',views.homepage3,name="homepage3"),
    path('bed_added/',views.bed_added,name="bed_added"),
    path('bed_removed/',views.bed_removed,name="bed_removed"),
    path('ventilator_added/',views.ventilator_added,name="ventilator_added"),
    path('ventilator_removed/',views.ventilator_removed,name="ventilator_removed"),
    path('iw_added/',views.iw_added,name="iw_added"),
    path('iw_removed/',views.iw_removed,name="iw_removed"),
    path('bed_occupied/',views.bed_occupied,name="bed_occupied"),
    path('bed_emptied/',views.bed_emptied,name="bed_emptied"),
    path('ventilator_occupied/',views.ventilator_occupied,name="ventilator_occupied"),
    path('ventilator_emptied/',views.ventilator_emptied,name="ventilator_emptied"),
    path('iw_occupied/',views.iw_occupied,name="iw_occupied"),
    path('iw_emptied/',views.iw_emptied,name="iw_emptied"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('adminbeds/',views.adminbeds,name="adminbeds"),
    path('adminventilators/',views.adminventilators,name="adminventilators"),
    path('adminiw/',views.adminiw,name="adminiw"),
    path('logout/',views.logout,name="logout"),
    path('changepassword/',views.changepassword,name="changepassword"),

]