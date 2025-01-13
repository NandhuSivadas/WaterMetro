from django.urls import path,include
from Guest import views
app_name="wguest"


urlpatterns = [
    path('UserRegistration/',views.userregistration,name='userregistration'),
    path('Login/',views.login,name='login'),
    path('',views.home_page,name='Homepage'),
    path('ForgetPassword/',views.ForgetPassword,name='forgetpassword'),
    path('otpver/', views.OtpVerification,name="verification"),
    path('ajaxemail/', views.ajaxemail,name="ajaxemail"),
    path('otpver/', views.OtpVerification,name="verification"),
    path('create/', views.CreateNewPass,name="create"),

    path('Google/', views.google,name="glog"), 
    path('GoogleVerify/', views.Gverify,name="Gverify"), 


    path('EmailValid/',views.emailvalid,name='emailvalid'),
    path('emailverification/',views.emailverification,name='emailverification'),
    

  
 

]