"""youPlace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from index.views import home, seemore, details, search
from posts.views import posts
from signup.views import signupUser, loginUser ,logoutUser

urlpatterns = [
    path('', home, name='home'),
    path('login/', loginUser, name='login'),
    path('signup/', signupUser, name='signup'),
    path('logout/', logoutUser, name='logout'),
    path('post/', posts, name="post"),
    path('search/', search, name="search"),
    path('details/<str:pk>/', details, name="details"), 
    path('more/', seemore, name='more'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)