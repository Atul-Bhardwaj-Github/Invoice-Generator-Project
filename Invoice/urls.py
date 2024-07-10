"""
URL configuration for Invoice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path("",userlogin,name="login"),
    path("home/",home,name="home"),
    path('admin/', admin.site.urls),
    path('logout/',logout_view,name="logout_view"),
    path("add_Client/",add_Client_Services,name="add_Client_Services"),
    path("serviceProvider/",serviceProvider,name="serviceProvider"),
    path("delete/<int:id>/",delete,name="delete"),
    path("edit/<int:id>/",edit,name="edit"),
    path("allClient/",display_clients,name="allClient"),
    path("All_report/",All_report,name="All_report"),
    path("delete_client/<int:id>/",delete_client,name="delete_client"),    
    path("edit_client/<int:id>/",edit_client,name="edit_client"),    
    path("report/<int:id>/",report,name="report"), 
    path("show/<int:id>/",show , name="show"),
    # path('pdf/<int:id>/',GeneratePdf.as_view(),name="myview"),
]
