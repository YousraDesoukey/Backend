"""Auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from API import  views
from AuthSocial import views as viewx
from myapp import views as viewsy
from sociallogin import views as viewz
from theapps import views as viewzz
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', views.UserList.as_view()),
    url(r'^usersocial/', viewx.UserSocialList.as_view()),
    url(r'^login/', viewsy.UserList2.as_view()),
    url(r'^logins/', viewz.UserList2.as_view()),
    url(r'^forgetPassword/$', viewzz.resetPass.as_view()),
    url(r'^changePassword/$', viewzz.changePass.as_view()),

]
