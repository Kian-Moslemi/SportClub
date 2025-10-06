from django.urls import path
from . import views


urlpatterns = [
    path('service/<int:service_id>/',views.schedule_view,name='schedule'),
    path('confirmation/<int:service_id>/<str:date>/<str:time>/',views.reserve,name='confirm'),
    path('aboutus/',views.aboutus,name='about'),
    path('callus/',views.callus,name='call'),
    path('services/',views.serviceus,name='service'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('signin/',views.sign_in,name='signin'),
    path('',views.home,name='home')
]

