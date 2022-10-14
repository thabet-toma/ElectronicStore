from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.home),
    path('home', views.home1),
    path('reg', views.reg),
    path('pc', views.pc),
    path('login', views.login),
    path('phones',views.phones),
    path('electronicTool',views.electronicTool),
    path('pro123',views.pro123),
    path('show/<int:id>',views.show),
    path('regProc',views.regProc),
    path('addproduct',views.addproduct),
    path('LOGOUT',views.logout),
    path('loginPro',views.loginPro),
    path('add_order',views.add_order, name='add_order'),
    path('isDeliver',views.isDeliver),
    path('filter',views.filter),
    path('about_us',views.about_us),
    path('deleteOrder',views.deleteOrder),

    
]
