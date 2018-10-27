"""business_rules URL Configuration

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
from rest_framework import routers
from topics import views as topic_views
from user_preferences import views as user_preferences_views
from utils import views as utils_views


router = routers.SimpleRouter()
router.register(r'topic', topic_views.TopicViewSet)
router.register(r'source', user_preferences_views.SourceViewSet)
router.register(r'topicUser', user_preferences_views.TopicUserViewSet)
router.register(r'ldamodelTopics', topic_views.LdaModelTopicsViewSet)
router.register(r'userDashboard', user_preferences_views.DashboardUserViewSet)
router.register(r'dateConversion', utils_views.DateConversionViewSet)
router.register(r'topicComparison', topic_views.TopicComparisonViewSet)
router.register(r'contentUser', user_preferences_views.ContentUserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += router.urls
