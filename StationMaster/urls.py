from django.urls import path,include
from StationMaster import views
app_name="WebStationMaster"


urlpatterns = [
    path('Service/',views.service,name='service'),
    path('MyProfile/',views.my_profile,name='myprofile'),
    path('EditProfile/',views.edit_profile,name='editprofile'),
    path('ChangePassword',views.changepassword,name='changepassword'),      
    path('HomePage/',views.home_page,name='homepage'),
    path('AssignBoat/',views.assignboat,name='assignboat'),
    path('Del_Service/<int:did>',views.del_service,name='del_service'),
    path('Update_Service/<int:did>',views.update_service,name='update_service'),
    path('Del_AssignBoat/<int:did>',views.del_assignboat,name='del_assignboat'),
    path('Update_assignboat/<int:did>',views.update_assignboat,name='update_assignboat'),
    path('viewticketbooking/',views.viewticketbooking,name="viewticketbooking"),
    path('userboat_assign/<int:id>',views.userboat_assign,name="userboat_assign"),
    path('refund/<int:id>',views.refund,name="refund"),
    path('Report/',views.report,name="report"),
    path('logout/',views.logout,name="logout"),

    path('ajaxreport/',views.ajaxreport,name="ajaxreport"),

    path('ViewEventBooking/',views.vieweventbooking,name='vieweventbooking'),
    path('user_eventboat_assign/<int:id>',views.user_eventboat_assign,name="user_eventboat_assign"),

    path('PrintCard/',views.printcard,name='printcard'),

]