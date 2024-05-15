from django.urls import path,include
from Guest import views
app_name="wguest"


urlpatterns = [
    path('UserRegistration/',views.userregistration,name='userregistration'),
    path('Login/',views.login,name='login'),
    path('',views.home_page,name='Homepage'),

    
 

]