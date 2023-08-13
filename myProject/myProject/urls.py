"""
URL configuration for myProject project.

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
from . import project_urls


urlpatterns = [
    path('about/', project_urls.about_view),
    path('', project_urls.nothing_view),
    path('<article>/', project_urls.article_view),
    path('<article>/comment/', project_urls.article_comment_view),
    path('create/', project_urls.create_view),
    path('<article>/update/', project_urls.article_update_view),
    path('<article>/delete/', project_urls.article_delete_view),
    path('topics/', project_urls.topics_view),
    path('topics/<topics>/subscribe/', project_urls.topics_subscribe_view),
    path('topics/<topics>/unsubscribe/', project_urls.topics_unsubscribe_view),
    path('profile/<str:username>/', project_urls.profile_username_view),
    path('set-password/', project_urls.setPassword_view),
    path('set-userdata/', project_urls.setUserdata_view),
    path('deactivate/', project_urls.deactivate_view),
    path('register/', project_urls.register_view),
    path('login/', project_urls.login_view),
    path('logout/', project_urls.logout_view),
]
